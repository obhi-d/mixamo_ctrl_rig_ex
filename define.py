# control rig
c_prefix = "Ctrl_"
c_root_name = "root"
master_rig_names = {"master": "Master"}
spine_rig_names = {"pelvis": "Hips", "spine1": "Spine", "spine2": "Spine1",
                   "spine3": "Spine2", "hips_free": "Hips_Free", "hips_free_helper": "Hips_Free_Helper"}
head_rig_names = {"neck": "Neck", "head": "Head"}
leg_rig_names = {
    "thigh_ik": "UpLeg_IK",
    "thigh_fk": "UpLeg_FK",
    "calf_ik": "Leg_IK",
    "calf_fk": "Leg_FK",
    "foot_fk": "Foot_FK",
    "foot_ik": "Foot_IK",
    "foot_snap": "Foot_Snap",
    "foot_ik_target": "Foot_IK_target",
    "foot_01": "Foot_01", 
    "foot_01_pole": "Foot_01_Pole", 
    "heel_out": "FootHeelOut", 
    "heel_in": "FootHeelIn", 
    "heel_mid": "FootHeelMid", 
    "toe_end": "ToeEnd", 
    "toe_end_01": "ToeEnd_01", 
    "toe_ik": "Toe_IK", 
    "toe_track": "ToeTrack", 
    "toe_01_ik": "Toe01_IK", 
    "toe_02": "Toe02", 
    "toe_fk": "Toe_FK", 
    "foot_roll_cursor": "FootRoll_Cursor", 
    "pole_ik": "LegPole_IK"
}

arm_rig_names = {
    "shoulder": "Shoulder", 
    "arm_ik": "Arm_IK", 
    "arm_fk": "Arm_FK", 
    "forearm_ik": "ForeArm_IK",
    "forearm_fk": "ForeArm_FK", 
    "pole_ik": "ArmPole_IK", 
    "hand_ik": "Hand_IK", 
    "hand_fk": "Hand_FK"
}

leg_chains = [
    "thigh",
    "calf",
    "foot",
    "toe"
]

arm_chains = [
    "arm",
    "forearm",
    "hand"
]

# mixamo bone names
spine_names = {"pelvis": "Hips", "spine1": "Spine",
               "spine2": "Spine1", "spine3": "Spine2"}
head_names = {"neck": "Neck", "head": "Head", "head_end": "HeadTop_End"}
leg_names = {"thigh": "UpLeg", "calf": "Leg",
             "foot": "Foot", "toe": "ToeBase", "toe_end": "Toe_End"}
arm_names = {"shoulder": "Shoulder", "arm": "Arm",
             "forearm": "ForeArm", "hand": "Hand"}
fingers_type = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
arm_twist_names = {"upperarm_twist": "upperarm_twist", "lowerarm_twist": "lowerarm_twist" }

mixamo_map = {
 "pelvis": "Hips", 
 "spine1": "Spine",
 "spine2": "Spine1", 
 "spine3": "Spine2",    
 "neck": "Neck", 
 "head": "Head", 
 "head_end": "HeadTop_End",
 "thigh": "UpLeg", 
 "calf": "Leg",
 "foot": "Foot", 
 "toe": "ToeBase", 
 "toe_end": "Toe_End", 
 "shoulder": "Shoulder", 
 "arm": "Arm",
 "forearm": "ForeArm", 
 "hand": "Hand"
}
