import time

class Clock:
	def __init__(self):
		self.last_time = time.perf_counter()

	def tick(self, fps=60):
		target_frame_time = 1.0 / fps
		now = time.perf_counter()
		elapsed = now - self.last_time
		sleep_time = max(0.0, target_frame_time - elapsed)

		if sleep_time > 0:
			time.sleep(sleep_time)

		self.last_time = time.perf_counter()
		return 1.0 / max(target_frame_time, elapsed)