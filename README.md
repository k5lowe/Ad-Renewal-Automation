# Ad-Renewal-Automation #
Renewing a Kijiji ad every 2 hours using the Selenium library for browser interaction and subprocess library for scheduling

## Description ##

This Python project automates the process of posting ads on Kijiji. The script automates the process of managing and posting ads on the Kijiji platform, ensuring a streamlined and efficient workflow. Given that Kijiji’s algorithm detects duplicate ads and penalizes repeated content, the automation smartly deletes existing ads before re-posting them to maintain compliance with platform rules. This also avoids clutter and helps keep the number of active ads manageable. It also supports running every 2 hours to ensure ads are frequently updated. The automation is built using Selenium for browser interaction and Python subprocess for scheduling.

Features:
- Automated login and ad posting on Kijiji.
- Scheduled task execution every 2 hours.
- Ability to delete or update specific ads based on title.
- Handles multiple images and file uploads efficiently.

Technologies:
- Python
- Selenium WebDriver
- Keyboard/Mouse Automation

## Notes ##

In my code, Kijiji_Ad_Automation, I initially hardcoded the login credentials directly in the script, but this is not a good security practice. A better approach is to store the login information in a separate, secure file (e.g., a text file or environment variables) and have the script read the credentials from there.

## Attributions & Remarks ##

The entirity of this project rested on the kind help of the following websites. As always, ChatGPT proved an immense help when nothing else worked (thank you Sam!).

- https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
- https://selenium-python.readthedocs.io/locating-elements.html#locating-elements
- https://thepythoncode.com/article/automate-login-to-websites-using-selenium-in-python
- https://www.youtube.com/watch?v=QLrf813RYL4&ab_channel=E4E-Learning
- https://www.reddit.com/r/selenium/comments/rnlpl5/how_to_click_on_a_button_in_python_using_selenium/
- https://stackoverflow.com/questions/75552030/how-can-i-print-out-all-text-in-a-web-table-column-in-python-using-selenium
- https://www.youtube.com/watch?v=ZohudLX9FfY&ab_channel=Let%27sKodeIt
- https://medium.com/@gbemiadekoya/importing-python-libraries-in-vs-code-e9e7806586a7


Please feel free to use this code! Lastly, any feedback on how to optimize this code would be greatly appreciated.
