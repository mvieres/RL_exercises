import gym

# choose the gym environment you want to run
env = gym.make("CartPole-v1", render_mode="human")

# reset the environment to its initial state
observation, info = env.reset()

while True:
    observation = env.reset()
    for _ in range(200):
        env.render()
        action = env.action_space.sample()
        observation, reward, terminated, truncuated, info = env.step(action)
        if terminated or truncuated:
            print(f"Game finished after {_ +1} steps.")
            break
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

env.close()