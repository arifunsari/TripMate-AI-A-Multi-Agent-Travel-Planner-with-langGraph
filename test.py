from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# res = tavily_search("Best hotels in Hyderabad for Biryani give me the name only having 5 start rating")
# print(res)


res = search_flights("Plan a 7 days Nepal trip from Bangladesh")
print(res)

# user_input = input("Enter travel request: ")

# response = run_travel_agent(
#     user_input=user_input,
#     thread_id="test_user"
#  )

# print("\nFINAL RESPONSE:\n")=
# print(response["answer"])


import os

print(os.getenv("LANGSMITH_API_KEY"))
print(os.getenv("LANGSMITH_TRACING"))
print(os.getenv("LANGSMITH_PROJECT"))