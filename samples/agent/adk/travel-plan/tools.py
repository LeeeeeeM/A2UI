# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import logging
import random
from datetime import datetime, timedelta

from google.adk.tools.tool_context import ToolContext

logger = logging.getLogger(__name__)


def plan_trip(departure: str, destination: str, travel_date: str, tool_context: ToolContext) -> str:
    """Call this tool to plan a trip and get flight information.

    Args:
        departure: Departure city
        destination: Destination city
        travel_date: Travel date in YYYY-MM-DD format
        tool_context: Tool context

    Returns:
        JSON string containing flight information
    """
    logger.info("--- TOOL CALLED: plan_trip ---")
    logger.info(f"  - Departure: {departure}")
    logger.info(f"  - Destination: {destination}")
    logger.info(f"  - Date: {travel_date}")

    # Generate mock flight data
    airlines = [
        {"name": "Air China", "code": "CA"},
        {"name": "China Eastern Airlines", "code": "MU"},
        {"name": "China Southern Airlines", "code": "CZ"},
        {"name": "Hainan Airlines", "code": "HU"},
        {"name": "Xiamen Airlines", "code": "MF"}
    ]

    flights = []
    for i in range(3):
        airline = random.choice(airlines)

        # Generate flight times
        departure_hour = random.randint(6, 18)  # 6 AM to 6 PM
        duration_hours = random.randint(8, 15)  # 8-15 hours for international flights
        duration_minutes = random.randint(0, 59)

        departure_time = f"{departure_hour:02d}:{random.randint(0, 59):02d} AM" if departure_hour < 12 else f"{departure_hour-12 or 12:02d}:{random.randint(0, 59):02d} PM"
        arrival_hour = (departure_hour + duration_hours) % 24
        arrival_time = f"{arrival_hour:02d}:{random.randint(0, 59):02d} AM" if arrival_hour < 12 else f"{arrival_hour-12 or 12:02d}:{random.randint(0, 59):02d} PM"

        flight_number = f"{airline['code']} {random.randint(100, 999)}"
        duration = f"{duration_hours}h {duration_minutes:02d}m"
        price = random.randint(3000, 8000)  # ¥3000-8000

        flight = {
            "airline": airline['name'],
            "flightNumber": flight_number,
            "departureTime": departure_time,
            "arrivalTime": arrival_time,
            "duration": duration,
            "price": f"¥{price}"
        }
        flights.append(flight)

    logger.info(f"  - Generated {len(flights)} flight options")

    return json.dumps(flights)
