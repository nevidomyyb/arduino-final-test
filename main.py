import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.monitoring import Monitoring
monitoring = Monitoring()
monitoring.draw()