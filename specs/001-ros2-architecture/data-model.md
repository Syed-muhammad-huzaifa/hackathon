# Data Model: ROS Architecture Chapter

## Entities

### Textbook Chapter

Represents the educational content for the "ROS Architecture" section.

*   **Name**: `ROS Architecture`
*   **Content**: Markdown text, diagrams, tables, examples.
*   **Word Count**: 600-800 words (constraint).
*   **Metadata**: Title, Part designation (Part II), learning objectives.

### Assessment

Represents the interactive component (e.g., quiz) designed to evaluate comprehension of the chapter. This will be implemented as a Custom React Component.

*   **Name**: `ROS Architecture Quiz`
*   **Questions**: A collection of `Question` entities.
*   **Pass Threshold**: A percentage or score required to pass (e.g., 80%).
*   **Feedback Mechanism**: How feedback is provided (e.g., immediate, summary).

### Question

A single question within an `Assessment`.

*   **ID**: Unique identifier.
*   **Text**: The question itself.
*   **Type**: (e.g., MultipleChoice, SingleChoice, ShortAnswer).
*   **Options**: A list of `Answer` entities (for multiple/single choice questions).
*   **CorrectAnswerID**: Reference to the correct `Answer` ID (or text for short answer).
*   **Explanation**: Optional explanation for the correct answer.

### Answer

A possible answer to a `Question`.

*   **ID**: Unique identifier.
*   **Text**: The text of the answer.

### UserResponse

The user's selected answer(s) for a `Question` in an `Assessment`.

*   **UserID**: Identifier for the user.
*   **AssessmentID**: Reference to the `Assessment` being taken.
*   **QuestionID**: Reference to the `Question` being answered.
*   **SelectedAnswerIDs**: List of `Answer` IDs chosen by the user.
*   **SubmittedText**: User's text input (for ShortAnswer questions).

### Score

The result of a user's attempt at an `Assessment`.

*   **UserID**: Identifier for the user.
*   **AssessmentID**: Reference to the `Assessment` taken.
*   **DateCompleted**: Timestamp of completion.
*   **RawScore**: Number of correct answers.
*   **PercentageScore**: Score as a percentage.
*   **Passed**: Boolean indicating if the pass threshold was met.
*   **FeedbackSummary**: Overall feedback based on performance.
