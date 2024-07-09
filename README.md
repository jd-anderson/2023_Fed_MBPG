# Paper
Code for our paper 
```
"Momentum for the Win: Collaborative Federated Reinforcement Learning across Heterogeneous Environments" 
Han Wang, Sihong He, Zhili Zhang, Fei Miao, James Anderson
ICML 2024
```

https://openreview.net/forum?id=g43yUNWX4V

# Requirements
pytorch 1.1.0  
[garage](https://github.com/rlworkgroup/garage) 2019.10.1\
[mujuco](http://www.mujoco.org/)  
[gym](https://github.com/openai/gym)  

# Usage

To run our algorithm
```
nohup python Fed_MBPG.py --env CartPole > Fed_MBPG_test_pin.out 2> Fed_MBPG_test_pin.err &
```

To run average baselines
```
nohup python Avg_MBPG.py --env CartPole > Avg_MBPG_test_pin.out 2> Avg_MBPG_test_pin.err &
```

To run different environments change --env to one of the following: "CartPole", "Walker", "Hopper" or "HalfCheetah". 

