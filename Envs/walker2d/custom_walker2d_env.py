import numpy as np
from gym.envs.mujoco import Walker2dEnv, HopperEnv, HalfCheetahEnv

class CustomWalker2dEnv(Walker2dEnv):

    def __init__(self, custom_low_bound=-0.005, custom_high_bound=0.005, **kwargs):
        super().__init__(**kwargs)  # 调用父类的初始化方法
        self.custom_low_bound = custom_low_bound
        self.custom_high_bound = custom_high_bound

    def reset_model(self):
        self.set_state(
            self.init_qpos
            + self.np_random.uniform(low=self.custom_low_bound, high=self.custom_high_bound, size=self.model.nq),
            self.init_qvel
            + self.np_random.uniform(low=self.custom_low_bound, high=self.custom_high_bound, size=self.model.nv),
        )
        return self._get_obs()