Feature: Signin module

  Scenario: Signup using invalid mobile number1
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then The invalid mobile number sequence is entered
    And The Continue button is clicked
    Then It should stay in the same page with a warning prompt

  Scenario: Signup using invalid mobile number2
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then The invalid mobile number sequence is entered  (0000000000)
    And The Continue button is clicked
    Then It should stay in the same page with a warning prompt2

  Scenario: Signup using invalid mobile number3
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then The invalid mobile number sequence is entered  (nodata)
    And The Continue button is clicked
    Then It should stay in the same page with a warning prompt3

  Scenario: Signup using invalid mobile number4
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then The invalid mobile number sequence is entered  (1)
    And The Continue button is clicked
    Then It should stay in the same page with a warning prompt3

  Scenario: Signup using invalid mobile number5
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then The invalid mobile number sequence is entered  (11111aaaaa)
    And The Continue button is clicked
    Then It should stay in the same page with a warning prompt3

  Scenario: Signup using invalid mobile number6
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then The invalid mobile number sequence is entered  (aaa!!!@@@b)
    And The Continue button is clicked
    Then It should stay in the same page with a warning prompt3

  Scenario: Signup using invalid mobile number7
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then The invalid mobile number sequence is entered  (111!!!@@@2)
    And The Continue button is clicked
    Then It should stay in the same page with a warning prompt3

  Scenario: Signup using valid mobile number8
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then A valid mobile number sequence is entered (9600415148)
    And The Continue button is clicked
    Then It proceeds to the OTP page

  Scenario: Signup using valid mobile number invalid OTP9
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then A valid mobile number sequence is entered (9600415148)
    And The Continue button is clicked
    Then It proceeds to the OTP page & invalid OTP sequence is entered (nodata)
    And The Submit button is clicked
    Then It stays in the OTP page

  Scenario: Signup using valid mobile number invalid OTP10
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then A valid mobile number sequence is entered (9600415148)
    And The Continue button is clicked
    Then It proceeds to the OTP page & invalid OTP sequence is entered (111111)
    And The Submit button is clicked
    Then It should stay in the same page with a warning prompt4

  Scenario: Signup using valid mobile number invalid OTP11
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then A valid mobile number sequence is entered (9600415148)
    And The Continue button is clicked
    Then It proceeds to the OTP page & invalid OTP sequence is entered (1)
    And The Submit button is clicked
    Then It should stay in the same page with a warning prompt4

  Scenario: Signup using valid mobile number valid OTP12
    Given The browser is opened and the website is loaded
    When The Login button on the website is clicked
    When Create your account is selected in the Login menu
    When The country dropdown gets clicked
    When India with the appropriate mobile extension is selected
    Then A valid mobile number sequence is entered (9600415148)
    And The Continue button is clicked
    Then It proceeds to the OTP page & valid OTP sequence is entered
    And The Submit button is clicked
    Then The account gets logged in

