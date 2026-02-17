from __future__ import annotations

from dataclasses import MISSING
from typing import Literal

from isaaclab.utils import configclass

from .rl_cfg import RslRlBaseRunnerCfg

#########################
# Policy configurations #
#########################
@configclass
class RslRlExtrinsicsDistillationStudentTeacherCfg:
    """Configuration for extrinsics distillation student-teacher network."""

    class_name: str = "StudentTeacherExtrinsics"

    extrinsics_output_dim: int = MISSING
    history_len: int = MISSING

    init_noise_std: float = MISSING
    noise_std_type: Literal["scalar", "log"] = "scalar"

    actor_obs_normalization: bool = MISSING
    priv_obs_normalization: bool = MISSING
    student_obs_normalization: bool = MISSING

    actor_hidden_dims: list[int] = MISSING
    teacher_extrinsics_hidden_dims: list[int] = MISSING

    activation: str = MISSING


############################
# Algorithm configurations #
############################
@configclass
class RslRlExtrinsicsDistillationAlgorithmCfg:
    """Configuration for extrinsics distillation algorithm."""

    class_name: str = "ExtrinsicsDistillation"

    num_learning_epochs: int = MISSING
    learning_rate: float = MISSING
    gradient_length: int = MISSING
    max_grad_norm: None | float = None

    optimizer: Literal["adam", "adamw", "sgd", "rmsprop"] = "adam"
    loss_type: Literal["mse", "huber"] = "mse"

#########################
# Runner configurations #
#########################

@configclass
class RslRlExtrinsicsDistillationRunnerCfg(RslRlBaseRunnerCfg):
    """Configuration for extrinsics distillation runner."""

    class_name: str = "ExtrinsicsDistillationRunner"

    policy: RslRlExtrinsicsDistillationStudentTeacherCfg = MISSING
    algorithm: RslRlExtrinsicsDistillationAlgorithmCfg = MISSING