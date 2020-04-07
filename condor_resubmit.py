import os
#Check which jobs failed

string_to_search = "preselected entries from root:"
path = "condor_logs/200405_072913"
condor_file_name = "submit_condor_jobs_lnujj"
Resubmission_txt = "_resubmit_2"

print 'grep -L  "'+string_to_search+'" '+ path + os.sep +'*.stdout'
output = os.popen('grep -L  "'+string_to_search+'" '+ path + os.sep +'*.stdout').read()

outjdl_file = open(condor_file_name+Resubmission_txt+".jdl","w")
with open(condor_file_name+".jdl") as myfile:
    head = [next(myfile) for x in xrange(7)]
print head

for lines in head:
  #outjdl_file.write(lines.replace(condor_file_name,condor_file_name+Resubmission_txt))
for lines in output.split():
  #print "="*51,"\n\n"
  #print lines.split('/')[2]
  #print "==> ",lines.strip()
  grep_output = os.popen('grep -E "Running.*root" '+lines.strip()).read()
  print grep_output
  #print "==> ",grep_output.split()[5].split('/')[-1]
  #root_file = grep_output.split()[5].split('/')[-1]
  #grep -A1 -B3 "034FD9B9-C376-2D4D-8BD8-B8848A1CB118.root" submit_condor_jobs_lnujj.jdl
  #print "---"
  #grep_condor_jdl_part = os.popen('grep -A1 -B3 "'+root_file+'" '+condor_file_name+'.jdl').read()
  #print grep_condor_jdl_part.replace('Process)','Process)'+Resubmission_txt)
  #outjdl_file.write(grep_condor_jdl_part.replace('Process)','Process)'+Resubmission_txt))
  #for grep_lines in grep_condor_jdl_part.split():
  #  print grep_lines.replace('Process)','Process)_resubmit_1')
  #print "---"
#outjdl_file.close()
#os.system('cp '+condor_file_name+'.sh  '+condor_file_name+Resubmission_txt+'.sh')
