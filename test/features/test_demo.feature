
@login @amazon
Feature: test demo aplication

#  Background: the amazon home page is displayed
  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Basic amazon Search
    Given the amazon home page is displayed
    When the user searches for "mobile phone"
    Then results are shown for "mobile phone"

  @successful
  Scenario: login to the amazon application
    Given go to the login page
    When user enter the email "manjit.1217@gmail.com"
    And user enter the password"Milan.1217"
    Then login successfull "Hello, manjit"

  Scenario: Outlined given, when, thens
    Given there are <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers
#    Examples: Vertical
#    | start | 12 | 2 |8|
#    | eat   | 5  | 1 |0|
#    | left  | 7  | 1 |3|