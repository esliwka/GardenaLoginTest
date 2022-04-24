# Login functional test cases

### Prerequisites: n/a

## TC: Login with correct credentials 
| Step # | Description | Test Data | Expected Result | Actual Result | Verdict |
|---|---|---|---|---|---|
| 1 | Navigate to: https://smart.gardena.com/ | "https://smart.gardena.com/" | Website reached | As expected | PASS |
| 2 | Input email in the Email field | "weyas57992@wowcg.com" | input entered | As expected | PASS |
| 3 | Input password in the Password field | "T3stP4ss" | input entered | As expected | PASS |
| 4 | Wait until Log In button becomes clickable |  | Log In button became clickable | As expected | PASS |
| 5 | Click Log In button |  | Log In button clicked | As expected | PASS |
| 6 | Wait until url matches Welcome Page |  | Url matches "https://smart.gardena.com/#/gateway-setup/welcome" | As expected | PASS |
## TC: Login with wrong password 
| Step # | Description | Test Data | Expected Result | Actual Result | Verdict |
|---|---|---|---|---|---|
| 1 | Navigate to: https://smart.gardena.com/ | "https://smart.gardena.com/" | Website reached | As expected | PASS |
| 2 | Input email in the Email field | "weyas57992@wowcg.com" | input entered | As expected | PASS |
| 3 | Input password in the Password field | "wrong" | input entered | As expected | PASS |
| 4 | Wait for Log In button to become clickable |  | Log In button became clickable | As expected | PASS |
| 5 | Click Log In button |  | Log In button clicked | As expected | PASS |
| 6 | Wait until error box is present |  | error box present | As expected | PASS |
| 7 | Check if error box message matches expected output |  | Error message matches "The email address and the password don't match." | As expected | PASS |
