import os,sys

year_campaign_dict = {
"v6_2016_campaign" : ["RunIISummer16NanoAODv6-*","Run2016*-Nano25Oct2019*-v*"],
"v6_2017_campaign" : ["RunIIFall17NanoAODv6-*","Run2017*-Nano25Oct2019*-v*"],
"v6_2018_campaign" : ["RunIIAutumn18NanoAODv6-*102X_upgrade2018_realistic_v20-v*","Run2018*-Nano25Oct2019*-v*"],
}

campaign_to_run = "v6_2016_campaign"
#campaign_to_run = "v6_2017_campaign"
#campaign_to_run = "v6_2018_campaign"

with open('input_data_Files/samples_list_das.dat') as in_file:
  count = 0
  outjdl_file = open("input_data_Files/sample_list_"+campaign_to_run+".dat","w")
  for lines in in_file:
     if lines[0] == "#":
       outjdl_file.write(lines)
       continue
     #if count > 27: break
     count = count +1
     print "="*51,"\n"
     print "==>  Sample : ",count
     print "==> line : ",lines
     sample_name = lines.split('/')[1]
     campaign = lines.split('/')[2]
     tier = lines.split('/')[3]
     #campaign = lines.split('/')[2].split('-')[0]
     print "==> DAS = ",lines
     print "==> sample_name = ",sample_name
     print "==> campaign = ",campaign
     print "==> campaign = ",tier
     if sample_name.find("SingleMuon") != -1 or sample_name.find("EGamma") != -1:
       v6_ntuples = "/"+sample_name+"/"+year_campaign_dict[campaign_to_run][1]+"/"+tier
     else:
       v6_ntuples = "/"+sample_name+"/"+year_campaign_dict[campaign_to_run][0]+"/"+tier
     #output = os.popen('dasgoclient --query="dataset='+lines.strip()+'"').read()
     print 'dasgoclient --query="dataset='+v6_ntuples.strip()+'"'
     output = os.popen('dasgoclient --query="dataset='+v6_ntuples.strip()+'"').read()
     print "output : ",output,"\n",type(output)," : ",len(output)
     if len(output.strip()) == 0:
        outjdl_file.write("# NOT FOUND: "+v6_ntuples.strip()+"\n")
     else:
        outjdl_file.write(output.strip()+"\n")
  outjdl_file.close()