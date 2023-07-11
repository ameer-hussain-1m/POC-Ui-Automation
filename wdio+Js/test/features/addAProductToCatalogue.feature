@regression @search
Feature: A user purchases items from a store
        Scenario:  A signed out user purchases item(s) from a designated store and verifies that the order is successfully sent.
        Given User opens the via application and checks he's not signed in
        When The user tries to login using the given credentials
        Then Verify the user has signed in
        When The user opens the Products page from the hamburger menu
        Then The user will be able to access the products page
        When The user click the add new item button