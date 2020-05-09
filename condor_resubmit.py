import os
#Check which jobs failed

string_to_search = "preselected entries from root:"
path = "condor_logs/Run2018_v6_3May/200503_031434/"
condor_file_name = "submit_condor_jobs_lnujj_v6_Run2018_v6_3May"
Resubmission_txt = "1"

grepCommand = 'grep -L  "'+string_to_search+'" '+ path + os.sep +'*.stdout'
grepCommand = grepCommand.replace('//','/')
print 'grep command: ',grepCommand
output = os.popen(grepCommand).read()

print('output:')
# print output
outjdl_file = open(condor_file_name+'_resubmit_'+Resubmission_txt+".jdl","w")
with open(condor_file_name+".jdl") as myfile:
    head = [next(myfile) for x in xrange(7)]
# print head

for lines in head:
  outjdl_file.write(lines)

for lines in output.split():
  print "==> ",lines.strip()
  grep_output = os.popen('grep -E "Running.*root" '+lines.strip()).read()
  # print grep_output
  root_file = grep_output.split()[5].split('/')[-1]
  grepCommand_GetJdlInfo = 'grep -A1 -B3 "'+root_file+'" '+condor_file_name+'.jdl'
  # print grepCommand_GetJdlInfo
  grep_condor_jdl_part = os.popen(grepCommand_GetJdlInfo).read()
  updateString = grep_condor_jdl_part.replace('Process)','Process)'+ '_resubmit_' +Resubmission_txt)
  # print updateString
  outjdl_file.write(updateString)
outjdl_file.close()