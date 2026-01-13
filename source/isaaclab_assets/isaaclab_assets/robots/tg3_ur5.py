import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
# from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR, ISAACLAB_NUCLEUS_DIR


def make_ur5_tactip_cfg(usd_path: str) -> ArticulationCfg:
    return ArticulationCfg(
        spawn=sim_utils.UsdFileCfg(
            usd_path=usd_path,
            rigid_props=sim_utils.RigidBodyPropertiesCfg(
                disable_gravity=True,
                max_depenetration_velocity=5.0,
            ),
            activate_contact_sensors=False,
            articulation_props=sim_utils.ArticulationRootPropertiesCfg(
                enabled_self_collisions=False,
                solver_position_iteration_count=16,
                solver_velocity_iteration_count=1,
            ),
            collision_props=sim_utils.CollisionPropertiesCfg(),
        ),
        init_state=ArticulationCfg.InitialStateCfg(
            joint_pos={
                "base_joint": 0.2051,
                "shoulder_joint": -1.9185,
                "elbow_joint": -2.0555,
                "wrist_1_joint": -0.78493,
                "wrist_2_joint": 1.5708,
                "wrist_3_joint": 0.0,
            }
        ),
        actuators={
            "shoulder": ImplicitActuatorCfg(
                joint_names_expr=["base_joint", "shoulder_joint"],
                effort_limit_sim=87.0,
                stiffness=200.0,
                damping=40.0,
            ),
            "elbow": ImplicitActuatorCfg(
                joint_names_expr=["elbow_joint"],
                effort_limit_sim=87.0,
                stiffness=200.0,
                damping=40.0,
            ),
            "wrist": ImplicitActuatorCfg(
                joint_names_expr=["wrist_.*"],
                effort_limit_sim=87.0,
                stiffness=200.0,
                damping=40.0,
            ),
        },
    )


UR5_TACTIP_CFG = make_ur5_tactip_cfg(
    "/home/bourne/IsaacLab/source/isaaclab_assets/data/Robots/tg3_asset/ur5_standard_tactip_edge.usd"
)

UR5_RA_TACTIP_CFG = make_ur5_tactip_cfg(
    "/home/bourne/IsaacLab/source/isaaclab_assets/data/Robots/tg3_asset/right_angle_tactip.usd"
)
