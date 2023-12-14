#### JSZ notes:
This repo is a modified copy of  the original [Logomotion](https://github.com/logo-to-lego/logomotion). The purpose here was to make it possible to use Logomotion as a Python package inside [Robottikoodieditori](https://github.com/robottikoodieditori/ohtuprojekti-robottikoodieditori) which is a browser-based code editor meant to make it easy for a teacher to have a classroom of students write Logo to control a Lego robot.

Small changes were also made to how error messages are generated. There were two reasons for this:

* error ranges were not produced correctly in `error_handler.py`. This was an issue for us because we wanted the editor to underline errors based on the `start` and `end` in the error message. This was mostly achieved. For example in a code such as
```
make "a 1
show "a + 1
```
`"a + 1` will be underlined as erroneous along with a message saying
```
message: You tried to do a calculation with something that is not a number.
line: 2
start: 6 - end: 11
```
* We would have liked all errors to be detected at once. This was not achieved. For example if we add a non parsable line to the previous example
```
make "a 1
show "a + 1
asdf
```
only the third line will be underlined and the message will be
```
message: I could not understand 'asdf'.
line: 3
start: 1 - end: 4
```
After fixing line 3 of course we get back to the situation in the first example.


*Original Logomotion README starts here:*
# Logomotion

![GitHub Actions](https://github.com/logo-to-lego/logomotion/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/logo-to-lego/logomotion/branch/main/graph/badge.svg?token=UTNJ6PS64G)](https://codecov.io/gh/logo-to-lego/logomotion)

## Purpose of the application
Logomotion is a Logo to Java compiler. The goal of the project is to enable the use of Logo programming language to control and instruct Lego Mindstorms robot model EV3, on the EV3dev operating system using the Java language. The primary purpose of this compiler is to provide educational assistance for children learning programming.

## Project progress
- [Product backlog](https://github.com/orgs/logo-to-lego/projects/1)
- [Sprint task board](https://github.com/orgs/logo-to-lego/projects/2)
- [Definition of done](#definition-of-done)
- [Working hours](https://docs.google.com/spreadsheets/d/12jyUsrNQjnxRyR_zxs0hcPKDV8_77uyjEEaTHGnhgDI)

## Documentation

- [Instructions](https://github.com/logo-to-lego/logomotion/blob/main/documentation/instructions.md)
- [Logo language](https://github.com/logo-to-lego/logomotion/blob/main/documentation/logo.md)
- [Logo language (Finnish)](https://github.com/logo-to-lego/logomotion/blob/main/documentation/logo_finnish.md)
- [Architecture](https://github.com/logo-to-lego/logomotion/blob/main/documentation/architecture.md)
- [Command structures](https://github.com/logo-to-lego/logomotion/blob/main/documentation/adding_command_structures.md)

## Definition of Done

* Pull requests from branches go through CI/CD pipeline successfully
* Code coverage percentage > 70%
* Pylint score should be 10/10


## Working practices

### Branching

Every PR is peer reviewed and must go through CI/CD pipeline before merging to trunk. Trunk should always contain working code.

## Where users can get help with your project
If you need help, please create a [Github issue](https://github.com/logo-to-lego/logomotion/issues/new/).
