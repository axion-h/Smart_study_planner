# Smart Study Planner with Pomodoro Timer

This is a simple **Smart Study Planner** that helps you plan your study schedule efficiently. The application allows you to:
- Add subjects with deadlines
- Generate a personalized study plan based on your available daily study hours
- Use a **Pomodoro timer** to stay focused and productive.

### **Features:**
1. **Subject Management**:
   - Add subjects with names and deadlines.
   - Delete subjects from the list.
   
2. **Study Plan Generation**:
   - Enter the available study hours per day.
   - Generate a study plan based on the deadlines of subjects.
   - The plan suggests study hours for each subject over the remaining days.

3. **Pomodoro Timer**:
   - A built-in **Pomodoro timer** to enhance focus. The timer runs for 25 minutes, followed by a break.
   - Start, stop, or reset the Pomodoro timer.

4. **Save the Plan**:
   - Save your study plan as a `.txt` file to refer to later.

### **Technologies Used:**
- **Python**: The application is developed using Python's **Tkinter** for the GUI.
- **Tkinter**: Used to create the GUI for input forms, buttons, and display.
- **tkcalendar**: Used for the date picker widget to select deadlines for subjects.

### **Installation:**

#### Requirements:
1. **Python 3.x**
2. Install the required dependencies:

```bash
pip install tkcalendar fpdf
