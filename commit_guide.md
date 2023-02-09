# Git Commit Description Guide

## Writting Format

Use conventional commit format like written below

>type(scope): Short description
>
>Message body
>
>breaking change
>
>Message footer

each part of formatting explanation
<ol>
    <li>type - the type of change you made to the repo</li>
    <li>scope - what part get changed</li>
    <li>short description - the short commit meesage pat (with maximum 50 characters)</li>
    <li>message body - the complete description of change on the code</li>
    <li>breaking change - the reason for a breaking change within the commit (optional)</li>
    <li>message footer - other description for multiple purpose. for example, to link the JIRA story that would be closed with applied changes (optional)</li>
</ol>

Below is the example of writting commit message with conventional format

>fix(foo): fix foo to enable bar
>
>This fixes the broken behavior of the component by doing xyz. 
>
>BREAKING CHANGE<br>
>Before this fix foo wasn't enabled at all, behavior changes from "<'old>" to "<new>"
>
>Closes D2IQ-12345

## The List of Commit Type

Choose one of a type from the list on below when writting commit description
<ol>
    <li>build – changes that affect the build system or external dependencies</li>
    <li>chore – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)</li>
    <li>ci – continuous integration related</li>
    <li>docs – updates to documentation such as a the README or other markdown files</li>
    <li>feat – a new feature is introduced with the changes</li>
    <li>fix – a bug fix has occurred</li>
    <li>perf – performance improvements</li>
    <li>revert – reverts a previous commit</li>
    <li>refactor – refactored code that neither fixes a bug nor adds a feature</li>
    <li>style – changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.</li>
    <li>test – including new or correcting previous tests</li>
</ol>











