import streamlit as st
from sympy import symbols, Eq, solve, diff, integrate, limit, Matrix
import time

def maths_tools():
    st.title("Math Equation Solver")
    st.write("Choose a math problem type to solve.")

    # Selectbox for choosing the type of problem
    problem_type = st.selectbox(
        "Select the type of math problem:",
        (
            "Equation Solver",
            "Differentiation",
            "Integration",
            "Linear Equations",
            "Quadratic Equations",
            "Limits",
            "Matrix Operations"
        )
    )

    # Define the symbol
    x = symbols('x')

    # Handle each problem type
    if problem_type == "Equation Solver":
        st.subheader("Equation Solver")
        equation_input = st.text_input("Enter the equation (e.g., 'x**2 - 4'): ")

        if equation_input:
            try:
                # Parse and solve the equation
                equation = Eq(eval(equation_input), 0)
                solutions = solve(equation, x)
                st.write(f"Solutions for the equation {equation_input} = 0:")
                st.write(solutions)
            except Exception as e:
                st.write(f"Error in solving equation: {e}")

    elif problem_type == "Differentiation":
        st.subheader("Differentiation")
        diff_input = st.text_input("Enter the function to differentiate (e.g., 'x**2 + 3*x'): ")

        if diff_input:
            try:
                # Parse and differentiate the function
                function = eval(diff_input)
                derivative = diff(function, x)
                st.write(f"Derivative of {diff_input} with respect to x:")
                st.write(derivative)
            except Exception as e:
                st.write(f"Error in differentiation: {e}")

    elif problem_type == "Integration":
        st.subheader("Integration")
        integrate_input = st.text_input("Enter the function to integrate (e.g., 'x**2 + 3*x'): ")

        if integrate_input:
            try:
                # Parse and integrate the function
                function = eval(integrate_input)
                integral = integrate(function, x)
                st.write(f"Integral of {integrate_input} with respect to x:")
                st.write(integral)
            except Exception as e:
                st.write(f"Error in integration: {e}")

    elif problem_type == "Linear Equations":
        st.subheader("Linear Equation Solver")
        a = st.number_input("Enter the coefficient of x (a): ", value=1.0)
        b = st.number_input("Enter the constant term (b): ", value=0.0)

        if st.button("Solve Linear Equation"):
            try:
                # Solve ax + b = 0
                equation = Eq(a * x + b, 0)
                solution = solve(equation, x)
                st.write(f"Solution for the equation {a}x + {b} = 0:")
                st.write(solution)
            except Exception as e:
                st.write(f"Error in solving linear equation: {e}")

    elif problem_type == "Quadratic Equations":
        st.subheader("Quadratic Equation Solver")
        a = st.number_input("Enter the coefficient of x^2 (a): ", value=1.0)
        b = st.number_input("Enter the coefficient of x (b): ", value=0.0)
        c = st.number_input("Enter the constant term (c): ", value=0.0)

        if st.button("Solve Quadratic Equation"):
            try:
                # Solve ax^2 + bx + c = 0
                equation = Eq(a * x**2 + b * x + c, 0)
                solutions = solve(equation, x)
                st.write(f"Solutions for the equation {a}x^2 + {b}x + {c} = 0:")
                st.write(solutions)
            except Exception as e:
                st.write(f"Error in solving quadratic equation: {e}")

    elif problem_type == "Limits":
        st.subheader("Limits")
        limit_input = st.text_input("Enter the function (e.g., 'sin(x)/x'): ")
        limit_point = st.number_input("Enter the point to approach: ", value=0.0)

        if limit_input:
            try:
                # Parse and find the limit
                function = eval(limit_input)
                limit_value = limit(function, x, limit_point)
                st.write(f"Limit of {limit_input} as x approaches {limit_point}:")
                st.write(limit_value)
            except Exception as e:
                st.write(f"Error in finding limit: {e}")

    elif problem_type == "Matrix Operations":
        st.subheader("Matrix Operations")
        matrix1_input = st.text_area("Enter the first matrix (e.g., '[[1, 2], [3, 4]]'): ")
        matrix2_input = st.text_area("Enter the second matrix (e.g., '[[5, 6], [7, 8]]'): ")

        operation = st.selectbox("Select an operation:", ("Add", "Subtract", "Multiply"))

        if matrix1_input and matrix2_input:
            try:
                # Parse the matrices
                matrix1 = Matrix(eval(matrix1_input))
                matrix2 = Matrix(eval(matrix2_input))

                # Perform the selected operation
                if operation == "Add":
                    result = matrix1 + matrix2
                elif operation == "Subtract":
                    result = matrix1 - matrix2
                elif operation == "Multiply":
                    result = matrix1 * matrix2

                st.write(f"Result of {operation.lower()}ing the matrices:")
                st.write(result)
            except Exception as e:
                st.write(f"Error in performing matrix operation: {e}")

def grade_calculator():
    st.title("Grade Calculator with What-If Analysis")
    st.write("Calculate your current grade and predict your final grade based on future performance.")

    # Input for number of assignments/tests
    num_grades = st.number_input("Enter the number of graded components (assignments, tests, etc.):", min_value=1, value=3)

    # Lists to store current grades and their weights
    current_grades = []
    weights = []

    # Collect current grades and weights
    st.subheader("Enter your current grades and their respective weights:")
    for i in range(num_grades):
        grade = st.number_input(f"Enter grade for component {i + 1} (out of 100):", min_value=0.0, max_value=100.0, value=0.0)
        weight = st.number_input(f"Enter weight for component {i + 1} (percentage of final grade):", min_value=0.0, max_value=100.0, value=0.0)
        current_grades.append(grade)
        weights.append(weight)

    # Calculate current weighted average
    current_weighted_average = None
    if sum(weights) != 100:
        st.warning("The sum of all weights must equal 100% to calculate the final grade correctly.")
    else:
        current_weighted_average = sum([grade * (weight / 100) for grade, weight in zip(current_grades, weights)])
        st.write(f"Your current weighted average is: {current_weighted_average:.2f}%")

    # What-If Analysis
    st.subheader("What-If Analysis")
    st.write("See how different future scores can affect your final grade.")

    # Input for What-If Analysis
    future_grade = st.number_input("Enter the potential future score (out of 100):", min_value=0.0, max_value=100.0, value=0.0)
    future_weight = st.number_input("Enter the weight of this future component (percentage of final grade):", min_value=0.0, max_value=100.0, value=0.0)

    # Calculate potential final grade if current_weighted_average is available
    if current_weighted_average is not None:
        if future_weight + sum(weights) > 100:
            st.warning("The total weights, including the future component, must not exceed 100%.")
        else:
            remaining_weight = 100 - sum(weights)
            if future_weight > remaining_weight:
                st.warning(f"The weight of the future component cannot exceed the remaining {remaining_weight}% of the final grade.")
            else:
                potential_final_grade = (current_weighted_average * (sum(weights) / 100)) + (future_grade * (future_weight / 100))
                st.write(f"Your potential final grade, if you score {future_grade}% on the future component, would be: {potential_final_grade:.2f}%")

def exam_anxiety_relief():
    st.title("Exam Anxiety Relief Tool")
    st.write("Use this tool to relieve exam stress through guided exercises and get productivity tips to manage your exam preparation.")

    # Section for Guided Meditation and Breathing Exercises
    st.subheader("Guided Meditation and Breathing Exercises")

    exercise_option = st.selectbox("Choose an exercise:", ["Deep Breathing", "Box Breathing", "Mindfulness Meditation"])

    if st.button("Start Exercise"):
        if exercise_option == "Deep Breathing":
            st.write("Follow the instructions for deep breathing:")
            st.write("1. Inhale slowly through your nose for 4 seconds.")
            time.sleep(4)
            st.write("2. Hold your breath for 4 seconds.")
            time.sleep(4)
            st.write("3. Exhale slowly through your mouth for 6 seconds.")
            time.sleep(6)
            st.write("4. Repeat this cycle 5 times.")
            st.success("Great job! You’ve completed the deep breathing exercise.")
        
        elif exercise_option == "Box Breathing":
            st.write("Follow the instructions for box breathing:")
            st.write("1. Inhale slowly through your nose for 4 seconds.")
            time.sleep(4)
            st.write("2. Hold your breath for 4 seconds.")
            time.sleep(4)
            st.write("3. Exhale slowly through your mouth for 4 seconds.")
            time.sleep(4)
            st.write("4. Hold your breath for 4 seconds.")
            time.sleep(4)
            st.write("5. Repeat this cycle 4 times.")
            st.success("Well done! You've completed the box breathing exercise.")
        
        elif exercise_option == "Mindfulness Meditation":
            st.write("Start with mindfulness meditation:")
            st.write("1. Sit comfortably with your eyes closed.")
            st.write("2. Focus on your breath and the sensation of air entering and leaving your body.")
            st.write("3. If your mind wanders, gently bring your attention back to your breath.")
            st.write("4. Continue this for 5-10 minutes.")
            st.success("You’ve completed the mindfulness meditation. Stay relaxed!")

    # Section for Productivity Tips
    st.subheader("Productivity Tips for Exam Preparation")
    st.write("""
        - **Create a Study Schedule**: Plan your study time, setting aside specific blocks for each subject.
        - **Break Tasks into Small Steps**: Divide large tasks into smaller, manageable steps to avoid feeling overwhelmed.
        - **Take Regular Breaks**: Use techniques like the Pomodoro method (25 minutes of study, followed by a 5-minute break).
        - **Stay Hydrated and Get Enough Sleep**: Taking care of your body helps improve concentration and memory.
        - **Set Realistic Goals**: Focus on what you can achieve in the given time and avoid cramming the night before an exam.
    """)

    st.info("Remember, exams are just a part of the learning process. Stay calm, prepare well, and take care of yourself!")

exam_anxiety_relief()

