Feature: Search google for stuff
  As a curious person
  I would like to seach google for stuff

Scenario: Stuff is found in first link
  Given I am at google
  When I search for "stuff"
  Then I see "stuff" in results
