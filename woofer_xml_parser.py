import os
import shutil
from os.path import expanduser


###### ROBOT PARAMETERS #####

## Solver params ##
woofer_timestep = 0.004					# timestep
woofer_solref = woofer_timestep*2		# time constant for contacts
woofer_armature = 0.0024				# armature for joints [kgm2]
woofer_solimp = "0.9 0.95 0.001"	# contact parameter

## Geometry params ##
woofer_mass = 8.0						# total robot mass
woofer_leg_radius = 0.02 				# radius of leg capsule
woofer_friction = 1.0					# friction between legs and ground
woofer_half_size = "0.33 0.088 0.046"	# half-size of body box
woofer_leg_fb = 0.23 					# front-back distance from center line to leg axis
woofer_leg_lr = 0.175 					# left-right distance from center line to leg plane
woofer_leg_geom = "0 0 0 0 0 -0.3"

## Joint params ##
woofer_joint_range = "-3 3"				# joint range in rads for angular joints
woofer_joint_force_range = "-12 12"		# force range for ab/ad and forward/back angular joints
woofer_ext_force_range = "-200 200"		# force range for radial/extension joint
woofer_ext_range = "-0.18 0.18"			# joint range for radial/extension joint
woofer_rad_damping = 2.0 				# damping on radial/extension joint [N/m/s]
woofer_joint_damping = 2.0				# damping on ab/ad and f/b angular joints [Nm/rad/s]


###### FILE PATHS  #####

dir_path = os.path.dirname(os.path.realpath(__file__))
in_file = dir_path+"/woofer.xml"

out_file = dir_path + "/woofer_out.xml"


### Parse the xml ###

print('Parsing MuJoCo XML file:')
print('Input xml: %s'%in_file)
print('Output xml: %s'%out_file)

with open(in_file, 'r') as file :
  filedata = file.read()


#### Replace variable names with values ####

# Solver specs
filedata = filedata.replace('woofer_timestep', str(woofer_timestep))
filedata = filedata.replace('woofer_solref', str(woofer_solref))
filedata = filedata.replace('woofer_friction', str(woofer_friction))
filedata = filedata.replace('woofer_armature', str(woofer_armature))
filedata = filedata.replace('woofer_solimp', str(woofer_solimp))

# Joint specs
filedata = filedata.replace('woofer_ext_force_range', str(woofer_ext_force_range))
filedata = filedata.replace('woofer_ext_range', str(woofer_ext_range))
filedata = filedata.replace('woofer_joint_range', str(woofer_joint_range))
filedata = filedata.replace('woofer_joint_force_range', str(woofer_joint_force_range))
filedata = filedata.replace('woofer_rad_damping', str(woofer_rad_damping))
filedata = filedata.replace('woofer_joint_damping', str(woofer_joint_damping))


# Geometry specs
filedata = filedata.replace('woofer_mass', str(woofer_mass))
filedata = filedata.replace('woofer_leg_radius', str(woofer_leg_radius))
filedata = filedata.replace('woofer_half_size', str(woofer_half_size))
filedata = filedata.replace('woofer_leg_fb', str(woofer_leg_fb))
filedata = filedata.replace('woofer_leg_lr', str(woofer_leg_lr))
filedata = filedata.replace("woofer_leg_geom", str(woofer_leg_geom))


# Write the xml file
with open(out_file, 'w') as file:
  file.write(filedata)