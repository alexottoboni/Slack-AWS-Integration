import os, sys
import urllib
import boto.ec2

def getState(region, instanceId):
   try:
      conn=boto.ec2.connect_to_region(region)
      reservations = conn.get_all_instances(instance_ids=[instanceId])
      for res in reservations:
         for inst in res.instances:
            if 'Name' in inst.tags:
               print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
            else:
               print "%s [%s]" % (inst.id, inst.state)
   except boto.exception.EC2ResponseError:
      return None

   return inst

if __name__ == "__main__":
   API_URL = %%MY_WEB_HOOK%%
   CHANNEL = %%MY_CHANNEL%%
   USERNAME = "server-bot"
   metadataURL = "http://instance-data/latest/meta-data/instance-id"
   instanceId = urllib.urlopen(metadataURL).read()
   guessRegion = os.environ['AWS_REGION']
   possibleRegions = ["us-west-1", "us-east-1", "eu-west-1"]
   state = getState(guessRegion, instanceId)
   if (state == None):
      for region in possibleRegions:
         state = getState(region, instanceId)
         if (state != None):
            break
   message = state.tags['Name'] + " (" + state.id + ") " + "is done booting"
   payload = "{\"channel\": " + "\"" + CHANNEL + "\", \"username\": " + "\"" + USERNAME + "\", \
   \"text\": " + "\"" + message + "\", \"icon_emoji\": \":computer:\"}' "
   os.system("curl -X POST --data-urlencode 'payload=" + payload + API_URL)
   sys.exit()
