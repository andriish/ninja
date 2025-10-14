#!/usr/bin/python3
#This script is designed to analyse the compilation databases created with cmake and imake build systems.
# The databases are created running build script with bear or bear3
#    sh CI/build.sh cmake tarball GNU bear3
#    sh CI/build.sh imake tarball GNU bear3
import json,re,sys,os
def get_compilation_DB(fname):
 f = open(fname)
 data = json.load(f)
 L = {}
 #return L
 for i in data:
  ar = i['arguments']
  fil = i['file']
  fil = fil.replace("//","/")
  fil = fil.replace("/builds/atlas-physics/pmg/mcexperts/powheg-experts/powheg-compilation/","")
  fil = fil.replace("/home/andriish/Projects/reference/VVJ/ORIG/","")
  current_directory = os.getcwd()
  fil = fil.replace(current_directory+"/","")
  fil = fil.replace("/builds/andriish/ttJ_MiNNLO/","")
  processes1=["Z2jet","W2jet","hvq","DMV","directphoton","Z_smeft","W_smeft","fourtops","gg_H_quark-mass-effects","DMGG","bbH","ttbarj","ttb_NLO_dec","ttH"]
  processes2=["ttJ_MiNNLO","Wj","Zj","WWJ","WW","ZZ","WZ","ggHH","ggHH_SMEFT","ggHZ","trijet","dijet","ST_wtch_DR","ST_wtch_DS","ST_sch","HWJ","HZJ"]
  processes3=["ST_tch_4f","Wgamma","Wbb_dec","Wbbj","Z_ew-BMNNPV","W_ew-BMNNP","DY_VLQ_NLO","DY_SLQ_NLO","h_bbg","ttZ","ttll"]
  processes4=["Zj/ZjMiNNLO","Wj/WjMiNNLO","HJJ","DMS_tloop","Wp_Wp_J_J","vbf_wp_wp","VBF_H","VBF_Wp_Wm","VBF_Z_Z","VBF_W-Z","ST_wtch_DR_modified"]
  processes5=["W","Z","Wtt_dec/pp_ttWm_EW", "Wtt_dec/pp_ttWm_QCD", "Wtt_dec/pp_ttWp_EW", "Wtt_dec/pp_ttWp_QCD"]
  processes6=["gg4l","HWJ_ew","HZJ_ew","b_bbar_4l","b_bbar_4l_modified","ttbb","LQ-s-chan","vbs-ssww-nloew"]
  processes7=["weakinos/chaIchaJ","weakinos/neuIneuJ","weakinos/neuIchaJ","b_bbar_4l_modified","HJ"]
  processes8=["WWJ","ZZJ","WZJ"]
  processes=processes1+processes2+processes3+processes4+processes5+processes6+processes7+processes8
  for p in processes:
    fil = fil.replace("POWHEG-BOX-V2/"+p+"/","User-Processes-V2/"+p+"/")
    fil = fil.replace("POWHEG-BOX-V2/weakinos/","User-Processes-V2/weakinos/")
    fil = fil.replace("POWHEG-BOX-NoUserProcesses/"+p+"/","POWHEG-BOX/"+p+"/")
    fil = fil.replace("POWHEG-BOX-NoUserProcesses","POWHEG-BOX")
    fil = fil.replace("POWHEG-BOX-RES/"+p+"/","User-Processes-RES/"+p+"/")
    if (re.match(r"^powheg-box-res-bb4l-sl-beta/"+p+"/",fil)):
      fil = fil.replace("powheg-box-res-bb4l-sl-beta/"+p+"/","User-Processes-powheg-box-res-bb4l-sl-beta/"+p+"/")
                        #powheg-box-res-bb4l-sl-beta/b_bbar_4l_modified/
  #print(fil)
  comp = ar[0]
  comparg = ar[1:]
  comparg = [ x.replace(current_directory+"","") for x in comparg]
  comparg = [ x for x in comparg if not re.match(r'^-I/usr/include$',x)]
  comparg = [ x for x in comparg if not re.match(r'^-J/POWHEG-BOX-V2/ttJ_MiNNLO/obj-gnu$',x)]
  comparg = [ x for x in comparg if not re.match(r'^-O2$',x)]
  comparg = [ x for x in comparg if not re.match(r'^-O0$',x)]
  comparg = [ x for x in comparg if not re.match(r'^-Dvirtual_EXPORTS$',x)]
  comparg = [ x for x in comparg if not re.match(r'^-fbounds-check$',x)]
  comparg = [ x for x in comparg if not re.match(r'^-fno-align-commons$',x)]
  comparg = [ x for x in comparg if x.startswith('-')]
  comparg = list( dict.fromkeys(comparg) )
  comparg.sort()
  if not re.match(r'.*process_obj.*',i['directory']) :
   L[fil] = comparg
 f.close()
 return L

def get_list_difference(li1, li2):
  return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def get_list(dict):
  list = []
  for key in dict.keys():
    list.append(key)
  return list

def main():
  if re.match(r'.*/POWHEG-BOX-V2/Wp_Wp_J_J.*',sys.argv[2]):
   return
    
  imakeDB = get_compilation_DB(sys.argv[1])
  cmakeDB = get_compilation_DB(sys.argv[2])
  if re.match(r'.*/weakinos/.*',sys.argv[2]):
    imakeDB2 = get_compilation_DB("REFERENCE/POWHEG-BOX-V2/weakinos/compile_commands.json")
    print(len(imakeDB2))
    imakeDB.update(imakeDB2)
  if re.match(r'.*RES/b_bbar_4l_modified/.*',sys.argv[2]):
    imakeDB2 = get_compilation_DB("REFERENCE/POWHEG-BOX-RES/b_bbar_4l_modified/Pwhg-so-ATLAS/compile_commands.json")
    print(len(imakeDB2))
    imakeDB.update(imakeDB2)

  cmakeList = get_list(cmakeDB)
  cmakeList.sort()

  imakeList = get_list(imakeDB)
  imakeList.sort()
  
  print(imakeList)
  print(cmakeList)

  differenceList = get_list_difference(imakeList,cmakeList)

  filt=[
r'.*b_bbar_4l_modified/Born_wdec.f',
r'.*b_bbar_4l_modified/LesHouches_wdec.f',
r'.*b_bbar_4l_modified/bbinit_wdec.f',
r'.*b_bbar_4l_modified/gen_radiation_wdec.f',
r'.*b_bbar_4l_modified/init_phys_wdec.f',
r'.*b_bbar_4l_modified/init_processes_wdec.f',
r'.*b_bbar_4l_modified/maxrat_wdec.f',
r'.*b_bbar_4l_modified/mintwrapper_wdec.f',
r'.*b_bbar_4l_modified/pwhg_semileptonic.f',
r'.*b_bbar_4l_modified/real_wdec.f',
r'.*b_bbar_4l_modified/semileptonic_init.f',
r'.*b_bbar_4l_modified/sigreal_wdec.f',
r'.*b_bbar_4l_modified/virtual_wdec.f',
r'.*b_bbar_4l_modified/write_counters_wdec.f',
r'.*b_bbar_4l/Born_wdec.f',
r'.*b_bbar_4l/LesHouches_wdec.f',
r'.*b_bbar_4l/bbinit_wdec.f',
r'.*b_bbar_4l/gen_radiation_wdec.f',
r'.*b_bbar_4l/init_phys_wdec.f',
r'.*b_bbar_4l/init_processes_wdec.f',
r'.*b_bbar_4l/maxrat_wdec.f',
r'.*b_bbar_4l/mintwrapper_wdec.f',
r'.*b_bbar_4l/pwhg_semileptonic.f',
r'.*b_bbar_4l/real_wdec.f',
r'.*b_bbar_4l/semileptonic_init.f',
r'.*b_bbar_4l/sigreal_wdec.f',
r'.*b_bbar_4l/virtual_wdec.f',
r'.*b_bbar_4l/write_counters_wdec.f',
r'.*process_obj.*',
r'.*downloadedqcdloop-src/.*',
r'.*OpenLoops/.*',
r'.*openloops2.f',
r'.*OpenLoopsStuff/openloops.f',
r'.*/lib_src/.*',
r'.*/write_mom.f',
r'.*/ffini.f',
r'.*/ff/ffinit_mine.f',
r'.*/ff/ffinit-save.f',
r'.*/ff/ffinit.f',
r'.*ST_wtch_DR_modified/Born.f.*',
r'.*ST_wtch_DR_modified/Born_phsp.f.*',
r'.*ggHH/foo/btilde_gghh.f.*',
r'.*ggHH/foo/sigremnants_gghh.f.*',
r'.*ggHH/btilde_gghh.f.*',
r'.*ggHH/sigremnants_gghh.f.*',
r'.*/LoopTools-2.12/.*',
r'.*Tools/programs.*',
r'.*gg_H_quark-mass-effects/btilde_gghh.f.*',
r'.*gg_H_quark-mass-effects/sigremnants_gghh.f.*',
r'.*gg_H_quark-mass-effects/btilde.f.*',
r'.*gg_H_quark-mass-effects/sigremnants.f.*'
]
  with open(sys.argv[3], 'w') as fp:
     for item in imakeList:
      pa=True
      for flt in filt:
        if re.match(flt,item):
          pa=False
      if re.match(r'.*/ST_wtch_DS/.*',sys.argv[2]) or re.match(r'.*/ST_wtch_DS/.*',sys.argv[1]):
        if  re.match(r'.*/sigreal.f',item): 
           pa=False
      if re.match(r'.*/gg_H_quark-mass-effects/.*',sys.argv[2]) or re.match(r'.*/gg_H_quark-mass-effects/.*',sys.argv[1]): 
         if re.match(r'.*/btilde_ggH.f',item) or re.match(r'.*/sigremnants_ggH.f',item) or re.match(r'.*/btilde.f',item) or re.match(r'.*/sigremnants.f',item): 
           pa=False
      if (pa):
        fp.write("%s\n" % item)

  with open(sys.argv[4], 'w') as fp:
     for item in cmakeList:
      pa=True
      for flt in filt:
        if re.match(flt,item):
          pa=False
      if re.match(r'.*/ST_wtch_DS/.*',sys.argv[2]) or re.match(r'.*/ST_wtch_DS/.*',sys.argv[1]):
        if  re.match(r'.*/sigreal.f',item): 
           pa=False
      if re.match(r'.*/gg_H_quark-mass-effects/.*',sys.argv[2]) or re.match(r'.*/gg_H_quark-mass-effects/.*',sys.argv[1]): 
         if re.match(r'.*/btilde_ggH.f',item) or re.match(r'.*/sigremnants_ggH.f',item) or re.match(r'.*/btilde.f',item) or re.match(r'.*/sigremnants.f',item): 
           pa=False
      if (pa):
        fp.write("%s\n" % item)

  print(differenceList)

main()
