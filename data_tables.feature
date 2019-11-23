Feature: Datatables

Scenario: I use datatables
    Given the following users exist:
      | name   | email              | twitter         |
      | Aslak  | aslak@cucumber.io  | @aslak_hellesoy |
      | Julien | julien@cucumber.io | @jbpros         |
      | Matt   | matt@cucumber.io   | @mattwynne      |
    When parameters exist:
      | https connection |
      | http connection  |
      | ftp connection   |
    Then I should see the following names:
      | name   |
      | Aslak  |
      | Julien |
      | Matt   |