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

TRAVEL_UI_EXAMPLES = """
---BEGIN TRAVEL_PLANNING_FORM_EXAMPLE---
[
  {{ "beginRendering": {{ "surfaceId": "default", "root": "root-column", "styles": {{ "primaryColor": "#00BFFF", "font": "Roboto" }} }} }},
  {{ "surfaceUpdate": {{
    "surfaceId": "default",
    "components": [
      {{ "id": "root-column", "component": {{ "Column": {{ "children": {{ "explicitList": ["title-heading", "form-container"] }} }} }} }},
      {{ "id": "title-heading", "component": {{ "Text": {{ "usageHint": "h1", "text": {{ "literalString": "Plan Your Trip" }} }} }} }},
      {{ "id": "form-container", "component": {{ "Column": {{ "children": {{ "explicitList": ["departure-input", "destination-input", "date-input", "submit-button"] }} }} }} }},
      {{ "id": "departure-input", "component": {{ "TextField": {{ "label": {{ "literalString": "Departure City" }}, "text": {{ "path": "/departure" }}, "textFieldType": "shortText" }} }} }},
      {{ "id": "destination-input", "component": {{ "TextField": {{ "label": {{ "literalString": "Destination City" }}, "text": {{ "path": "/destination" }}, "textFieldType": "shortText" }} }} }},
      {{ "id": "date-input", "component": {{ "DateTimeInput": {{ "value": {{ "path": "/travelDate" }}, "enableDate": true, "enableTime": false }} }} }},
      {{ "id": "submit-button", "component": {{ "Button": {{ "child": "submit-text", "primary": true, "action": {{ "name": "plan_trip", "context": [ {{ "key": "departure", "value": {{ "path": "/departure" }} }}, {{ "key": "destination", "value": {{ "path": "/destination" }} }}, {{ "key": "travelDate", "value": {{ "path": "/travelDate" }} }} ] }} }} }} }},
      {{ "id": "submit-text", "component": {{ "Text": {{ "text": {{ "literalString": "Find Flights" }} }} }} }}
    ]
  }} }},
  {{ "dataModelUpdate": {{
    "surfaceId": "default",
    "path": "/",
    "contents": [
      {{ "key": "departure", "valueString": "" }},
      {{ "key": "destination", "valueString": "" }},
      {{ "key": "travelDate", "valueString": "" }}
    ]
  }} }}
]
---END TRAVEL_PLANNING_FORM_EXAMPLE---

---BEGIN FLIGHT_RESULTS_EXAMPLE---
[
  {{ "beginRendering": {{ "surfaceId": "default", "root": "root-column", "styles": {{ "primaryColor": "#00BFFF", "font": "Roboto" }} }} }},
  {{ "surfaceUpdate": {{
    "surfaceId": "default",
    "components": [
      {{ "id": "root-column", "component": {{ "Column": {{ "children": {{ "explicitList": ["title-heading", "flight-list"] }} }} }} }},
      {{ "id": "title-heading", "component": {{ "Text": {{ "usageHint": "h1", "text": {{ "path": "title" }} }} }} }},
      {{ "id": "flight-list", "component": {{ "List": {{ "direction": "vertical", "children": {{ "template": {{ "componentId": "flight-card-template", "dataBinding": "/flights" }} }} }} }} }},
      {{ "id": "flight-card-template", "component": {{ "Card": {{ "child": "flight-layout" }} }} }},
      {{ "id": "flight-layout", "component": {{ "Column": {{ "children": {{ "explicitList": ["flight-info", "flight-details", "flight-price"] }} }} }} }},
      {{ "id": "flight-info", "component": {{ "Row": {{ "children": {{ "explicitList": ["airline-text", "flight-number"] }} }} }} }},
      {{ "id": "airline-text", "component": {{ "Text": {{ "usageHint": "h4", "text": {{ "path": "airline" }} }} }} }},
      {{ "id": "flight-number", "component": {{ "Text": {{ "text": {{ "path": "flightNumber" }} }} }} }},
      {{ "id": "flight-details", "component": {{ "Row": {{ "children": {{ "explicitList": ["departure-time", "arrow", "arrival-time", "duration"] }} }} }} }},
      {{ "id": "departure-time", "component": {{ "Text": {{ "text": {{ "path": "departureTime" }} }} }} }},
      {{ "id": "arrow", "component": {{ "Text": {{ "text": {{ "literalString": " → " }} }} }} }},
      {{ "id": "arrival-time", "component": {{ "Text": {{ "text": {{ "path": "arrivalTime" }} }} }} }},
      {{ "id": "duration", "component": {{ "Text": {{ "text": {{ "path": "duration" }} }} }} }},
      {{ "id": "flight-price", "component": {{ "Text": {{ "usageHint": "h3", "text": {{ "path": "price" }} }} }} }}
    ]
  }} }},
  {{ "dataModelUpdate": {{
    "surfaceId": "default",
    "path": "/",
    "contents": [
      {{ "key": "title", "valueString": "Available Flights" }},
      {{ "key": "flights", "valueMap": [
        {{ "key": "flight1", "valueMap": [
          {{ "key": "airline", "valueString": "American Airlines" }},
          {{ "key": "flightNumber", "valueString": "AA 1234" }},
          {{ "key": "departureTime", "valueString": "08:00 AM" }},
          {{ "key": "arrivalTime", "valueString": "02:30 PM" }},
          {{ "key": "duration", "valueString": "6h 30m" }},
          {{ "key": "price", "valueString": "$450" }}
        ] }},
        {{ "key": "flight2", "valueMap": [
          {{ "key": "airline", "valueString": "Delta Airlines" }},
          {{ "key": "flightNumber", "valueString": "DL 5678" }},
          {{ "key": "departureTime", "valueString": "10:15 AM" }},
          {{ "key": "arrivalTime", "valueString": "04:45 PM" }},
          {{ "key": "duration", "valueString": "6h 30m" }},
          {{ "key": "price", "valueString": "$425" }}
        ] }},
        {{ "key": "flight3", "valueMap": [
          {{ "key": "airline", "valueString": "United Airlines" }},
          {{ "key": "flightNumber", "valueString": "UA 9012" }},
          {{ "key": "departureTime", "valueString": "02:30 PM" }},
          {{ "key": "arrivalTime", "valueString": "09:00 PM" }},
          {{ "key": "duration", "valueString": "6h 30m" }},
          {{ "key": "price", "valueString": "$480" }}
        ] }}
      ] }}
    ]
  }} }}
]
---END FLIGHT_RESULTS_EXAMPLE---
"""