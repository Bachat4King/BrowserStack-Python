Feature: demoqa tests

  Scenario: filling form with valid data
    Given go to https://demoqa.com/text-box
    When demoqa-textbox: fill the form with valid data
    And demoqa-textbox: click submit button
    Then the data is displayed on the page
