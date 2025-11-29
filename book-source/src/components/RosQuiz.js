import React, { useState } from 'react';

// Example questions data based on the ROS Architecture chapter and Data Model entities
const quizQuestions = [
  {
    id: 1,
    questionText: 'What is the primary purpose of a ROS Node?',
    type: 'SingleChoice',
    answerOptions: [
      { id: 'a', answerText: 'To serve as a physical robot component.', isCorrect: false },
      { id: 'b', answerText: 'To perform a specific computation within the ROS system.', isCorrect: true },
      { id: 'c', answerText: 'To establish a network connection outside the robot.', isCorrect: false },
      { id: 'd', answerText: 'To store persistent data for the entire robotic system.', isCorrect: false },
    ],
    explanation: 'A ROS Node is an executable process that performs computation, serving as a modular building block.',
  },
  {
    id: 2,
    questionText: 'Which ROS 2 communication mechanism is best suited for continuous data streams like sensor readings?',
    type: 'SingleChoice',
    answerOptions: [
      { id: 'a', answerText: 'Services', isCorrect: false },
      { id: 'b', answerText: 'Actions', isCorrect: false },
      { id: 'c', answerText: 'Topics', isCorrect: true },
      { id: 'd', answerText: 'Parameters', isCorrect: false },
    ],
    explanation: 'Topics are designed for asynchronous, one-way communication of continuous data streams.',
  },
  {
    id: 3,
    questionText: 'The computational graph in ROS 2 describes:',
    type: 'MultipleChoice',
    answerOptions: [
      { id: 'a', answerText: 'The network of ROS 2 nodes and their connections.', isCorrect: true },
      { id: 'b', answerText: 'The physical wiring diagram of the robot hardware.', isCorrect: false },
      { id: 'c', answerText: 'The data flow and communication pathways within a running ROS 2 system.', isCorrect: true },
      { id: 'd', answerText: 'The specific algorithms used by individual nodes.', isCorrect: false },
    ],
    explanation: 'The computational graph visually represents the network of nodes and their interconnections via topics, services, and actions, showing data flow.',
  },
  {
    id: 4,
    questionText: 'Briefly explain the main difference between ROS 2 Services and Actions.',
    type: 'ShortAnswer',
    correctAnswer: 'Services are synchronous request/reply for short tasks. Actions are asynchronous for long-running, preemptable tasks with feedback.', // This would typically be matched with a fuzzy logic or keyword search
    explanation: 'Services are for immediate, short-duration tasks (request-response). Actions are for long-running, preemptable tasks where feedback and cancellation are important.',
  },
];

const RosQuiz = () => {
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({}); // Stores {questionId: [selectedAnswerIds] or 'short answer text'}
  const [showResults, setShowResults] = useState(false);
  const [score, setScore] = useState(0);

  const currentQuestion = quizQuestions[currentQuestionIndex];

  const handleAnswerChange = (questionId, answer) => {
    setUserAnswers(prev => ({
      ...prev,
      [questionId]: answer,
    }));
  };

  const handleNextQuestion = () => {
    if (currentQuestionIndex < quizQuestions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      calculateResults();
      setShowResults(true);
    }
  };

  const calculateResults = () => {
    let newScore = 0;
    quizQuestions.forEach(q => {
      const userAnswer = userAnswers[q.id];
      if (q.type === 'SingleChoice' || q.type === 'MultipleChoice') {
        const correctOptions = q.answerOptions.filter(opt => opt.isCorrect).map(opt => opt.id);
        const userSelectedOptions = Array.isArray(userAnswer) ? userAnswer : [userAnswer].filter(Boolean); // Ensure it's an array for multiple choice

        // Simple comparison: check if all correct options are selected and no incorrect ones
        const isCorrect = correctOptions.length === userSelectedOptions.length &&
                          correctOptions.every(opt => userSelectedOptions.includes(opt));
        if (isCorrect) {
          newScore++;
        }
      } else if (q.type === 'ShortAnswer') {
        // For short answer, a simple check if the correct answer is contained (can be improved)
        if (userAnswer && q.correctAnswer && userAnswer.toLowerCase().includes(q.correctAnswer.toLowerCase().split(' ')[0])) {
             newScore++;
        }
      }
    });
    setScore(newScore);
  };

  if (showResults) {
    return (
      <div className="quiz-results">
        <h2>Quiz Results</h2>
        <p>You scored {score} out of {quizQuestions.length}!</p>
        {quizQuestions.map(q => (
          <div key={q.id} className="question-result">
            <p><strong>Q:</strong> {q.questionText}</p>
            {q.type === 'SingleChoice' || q.type === 'MultipleChoice' ? (
              <p>
                Your Answer:{' '}
                {q.answerOptions.filter(opt => (Array.isArray(userAnswers[q.id]) ? userAnswers[q.id].includes(opt.id) : userAnswers[q.id] === opt.id))
                              .map(opt => opt.answerText).join(', ') || 'No answer'}
              </p>
            ) : (
              <p>Your Answer: {userAnswers[q.id] || 'No answer'}</p>
            )}
            <p><strong>Correct Answer:</strong> {q.type === 'ShortAnswer' ? q.correctAnswer : q.answerOptions.filter(opt => opt.isCorrect).map(opt => opt.answerText).join(', ')}</p>
            <p><em>Explanation:</em> {q.explanation}</p>
            <hr />
          </div>
        ))}
        <button onClick={() => { setCurrentQuestionIndex(0); setUserAnswers({}); setShowResults(false); setScore(0); }}>Retake Quiz</button>
      </div>
    );
  }

  return (
    <div className="quiz-card">
      <div className="quiz-progress">
        Question {currentQuestionIndex + 1} of {quizQuestions.length}
      </div>
      <div className="quiz-question">
        <h3>{currentQuestion.questionText}</h3>
        <div className="quiz-answers">
          {currentQuestion.type === 'SingleChoice' && currentQuestion.answerOptions.map(option => (
            <button
              key={option.id}
              onClick={() => handleAnswerChange(currentQuestion.id, option.id)}
              className={userAnswers[currentQuestion.id] === option.id ? 'selected' : ''}
            >
              {option.answerText}
            </button>
          ))}
          {currentQuestion.type === 'MultipleChoice' && currentQuestion.answerOptions.map(option => (
            <button
              key={option.id}
              onClick={() => {
                const currentSelections = Array.isArray(userAnswers[currentQuestion.id]) ? [...userAnswers[currentQuestion.id]] : [];
                if (currentSelections.includes(option.id)) {
                  handleAnswerChange(currentQuestion.id, currentSelections.filter(item => item !== option.id));
                } else {
                  handleAnswerChange(currentQuestion.id, [...currentSelections, option.id]);
                }
              }}
              className={Array.isArray(userAnswers[currentQuestion.id]) && userAnswers[currentQuestion.id].includes(option.id) ? 'selected' : ''}
            >
              {option.answerText}
            </button>
          ))}
          {currentQuestion.type === 'ShortAnswer' && (
            <input
              type="text"
              value={userAnswers[currentQuestion.id] || ''}
              onChange={(e) => handleAnswerChange(currentQuestion.id, e.target.value)}
              placeholder="Type your answer here..."
            />
          )}
        </div>
      </div>
      <button onClick={handleNextQuestion} disabled={!userAnswers[currentQuestion.id]}>
        {currentQuestionIndex === quizQuestions.length - 1 ? 'Finish Quiz' : 'Next Question'}
      </button>
    </div>
  );
};

export default RosQuiz;