import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
# from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR, ISAACLAB_NUCLEUS_DIR


UR5_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/bourne/IsaacLab/source/isaaclab_assets/data/Robots/tg3_asset/ur5_standard_tactip_edge.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        activate_contact_sensors=False,
        # articulation_props=sim_utils.ArticulationRootPropertiesCfg(
        #     enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0
        # ),
        # collision_props=sim_utils.CollisionPropertiesCfg(contact_offset=0.005, rest_offset=0.0),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={ 
            "base_joint": 0.2051,
            "shoulder_joint": -1.9185,
            "elbow_joint": -2.0555,
            "wrist_1_joint": -0.78493,
            "wrist_2_joint": 1.5708,
            "wrist_3_joint": 0.0,
        },
        pos=(0.0, 0.0, 0.0),
        rot=(1.0, 0.0, 0.0, 0.0),
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=[".*"],
            effort_limit_sim=87.0,
            stiffness=800.0,
            damping=40.0,
        ),
    },
)