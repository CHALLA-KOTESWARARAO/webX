import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webXProj.settings")
django.setup()

from interviewprep.models import Question

print("\n🗑 Clearing old questions...")
Question.objects.all().delete()
print("✔ Cleared successfully!\n")

data = [

# ================= FRONTEND ==================
# HTML (20)
("Frontend", "HTML", "Which HTML tag is used to create a hyperlink?", ["<a>", "<link>", "<url>", "<href>"], "A"),
("Frontend", "HTML", "Which tag defines the largest heading?", ["<h6>", "<header>", "<h1>", "<head>"], "C"),
("Frontend", "HTML", "Which tag is used for inserting an image?", ["<img>", "<src>", "<image>", "<pic>"], "A"),
("Frontend", "HTML", "Which attribute gives alternative text to images?", ["title", "src", "alt", "href"], "C"),
("Frontend", "HTML", "Which tag is used for input fields?", ["<input>", "<form>", "<textfield>", "<text>"], "A"),
("Frontend", "HTML", "Which element contains metadata?", ["<body>", "<meta>", "<head>", "<script>"], "C"),
("Frontend", "HTML", "Which tag creates a dropdown?", ["<select>", "<dropdown>", "<list>", "<input>"], "A"),
("Frontend", "HTML", "HTML stands for?", ["Hyper Trainer Marking Language", "HyperText Markup Language", "HyperText Markdown Language", "None"], "B"),
("Frontend", "HTML", "Which tag is used for lists?", ["<ul>", "<p>", "<h1>", "<table>"], "A"),
("Frontend", "HTML", "To make text bold:", ["<b>", "<strong>", "<p>", "Both A & B"], "D"),
("Frontend", "HTML", "Which tag defines a table row?", ["<td>", "<tr>", "<th>", "<table>"], "B"),
("Frontend", "HTML", "Which tag defines a form?", ["<form>", "<input>", "<body>", "<div>"], "A"),
("Frontend", "HTML", "Which tag embeds a video?", ["<video>", "<movie>", "<media>", "<play>"], "A"),
("Frontend", "HTML", "Which element defines navigation links?", ["<nav>", "<header>", "<footer>", "<menu>"], "A"),
("Frontend", "HTML", "Which is a block-level element?", ["<span>", "<div>", "<b>", "<i>"], "B"),
("Frontend", "HTML", "Which tag forces a new line?", ["<span>", "<hr>", "<br>", "<p>"], "C"),
("Frontend", "HTML", "The root element of an HTML page:", ["<html>", "<DOCTYPE>", "<body>", "<title>"], "A"),
("Frontend", "HTML", "Which tag is self-closing?", ["<img>", "<div>", "<p>", "<table>"], "A"),
("Frontend", "HTML", "Input type for password?", ["text", "password", "secure", "code"], "B"),
("Frontend", "HTML", "Semantic tag:", ["<div>", "<span>", "<article>", "<b>"], "C"),

# CSS (20)
("Frontend", "CSS", "CSS stands for?", ["Cascade Style Sheets", "Cascading Style Sheets", "Color Style Syntax", "Code Styling System"], "B"),
("Frontend", "CSS", "Which property changes text color?", ["font-color", "color", "text-style", "bgcolor"], "B"),
("Frontend", "CSS", "Which unit is relative to root font size?", ["em", "px", "rem", "%"], "C"),
("Frontend", "CSS", "Which creates a flex container?", ["display:flex", "flex:true", "position:flex", "flexbox"], "A"),
("Frontend", "CSS", "Which property sets the background color?", ["background-color", "bgcolor", "color", "background-style"], "A"),
("Frontend", "CSS", "Which CSS uses ID selector?", ["#", ".", ":", "*"], "A"),
("Frontend", "CSS", "Which property sets the font size?", ["text-size", "font-size", "size", "fontsize"], "B"),
("Frontend", "CSS", "How do you make text bold?", ["font-style:bold", "font-weight:bold", "text:bold", "bold:true"], "B"),
("Frontend", "CSS", "Which property adds space inside the element?", ["margin", "padding", "border", "gap"], "B"),
("Frontend", "CSS", "Which property is used for rounded corners?", ["corner-radius", "border-radius", "round-corner", "shape-radius"], "B"),
("Frontend", "CSS", "Default position property value?", ["fixed", "absolute", "relative", "static"], "D"),
("Frontend", "CSS", "Which property controls the stacking order?", ["index", "z-index", "stack", "order"], "B"),
("Frontend", "CSS", "Which display type hides the element but reserves its space?", ["display:none", "visibility:hidden", "opacity:0", "hidden:true"], "B"),
("Frontend", "CSS", "How to set a background image?", ["background:url(image)", "image:url()", "bg-image:()", "background-img()"], "A"),
("Frontend", "CSS", "Which property aligns text horizontally?", ["align", "justify", "text-align", "text-position"], "C"),
("Frontend", "CSS", "Which unit is relative to parent font size?", ["px", "em", "rem", "pt"], "B"),
("Frontend", "CSS", "Which property makes content scrollable?", ["scroll", "overflow", "slide", "scrolling"], "B"),
("Frontend", "CSS", "Which one selects all paragraph tags?", ["#p", ".p", "p", "*p"], "C"),
("Frontend", "CSS", "CSS flex-direction default value?", ["row", "column", "reverse", "flex"], "A"),
("Frontend", "CSS", "Which selector targets immediate child elements?", ["A B", "A > B", "A + B", "A ~ B"], "B"),

# ================= JS (20)
("Frontend", "JS", "Which keyword declares a block-scoped variable?", ["var", "let", "const", "static"], "B"),
("Frontend", "JS", "Which method converts JSON to JavaScript object?", ["JSON.stringify()", "JSON.parse()", "parse.JSON()", "Object.parse()"], "B"),
("Frontend", "JS", "Which symbol is used for strict equality check?", ["==", "===", "!=", "="], "B"),
("Frontend", "JS", "What is the output type of typeof null?", ["object", "null", "undefined", "boolean"], "A"),
("Frontend", "JS", "Which function is used to delay execution?", ["setInterval()", "setTimeout()", "wait()", "delay()"], "B"),
("Frontend", "JS", "How to write a comment in JavaScript?", ["<!--comment-->", "* comment *", "# comment", "// comment"], "D"),
("Frontend", "JS", "Which of the following is not a JS data type?", ["String", "Boolean", "Float", "Object"], "C"),
("Frontend", "JS", "Which built-in method removes last element of array?", ["shift()", "pop()", "remove()", "delete"], "B"),
("Frontend", "JS", "Which operator spreads array elements?", ["...", "??", "+", "**"], "A"),
("Frontend", "JS", "Which method selects element by ID?", ["getElementsByClass", "querySelectorAll()", "getElementById()", "$()"], "C"),
("Frontend", "JS", "Which object handles browser alerts?", ["console", "window", "document", "navigator"], "B"),
("Frontend", "JS", "Which array method returns new filtered array?", ["map()", "filter()", "sort()", "slice()"], "B"),
("Frontend", "JS", "Which keyword stops loop execution?", ["break", "stop", "halt", "end"], "A"),
("Frontend", "JS", "Which of these defines a function?", ["func my()", "function my()", "define my()", "method my()"], "B"),
("Frontend", "JS", "Which method adds an element to end of array?", ["push()", "add()", "insert()", "append()"], "A"),
("Frontend", "JS", "What is NaN?", ["Not a Number", "No use", "Null as Number", "Negative Array Number"], "A"),
("Frontend", "JS", "Which method converts string to integer?", ["parseInt()", "int()", "strToInt()", "stringToNumber()"], "A"),
("Frontend", "JS", "Promises represent?", ["Errors only", "Data only", "Future value", "Loop"], "C"),
("Frontend", "JS", "Arrow functions were introduced in?", ["ES4", "ES5", "ES6", "ES7"], "C"),
("Frontend", "JS", "LocalStorage stores data for?", ["Page session only", "Until manually cleared", "Only 24 hours", "Only in RAM"], "B"),

# ================= React (20)
("Frontend", "React", "What is React mainly used for?", ["Database", "Styling", "Building UI", "Security"], "C"),
("Frontend", "React", "JSX stands for?", ["JavaScript XML", "Java Syntax Extension", "JSON XML", "None"], "A"),
("Frontend", "React", "Which hook manages state?", ["useState()", "useEffect()", "useMemo()", "useRef()"], "A"),
("Frontend", "React", "Which helps handling side-effects?", ["useContext()", "useEffect()", "useReducer()", "useDebug()"], "B"),
("Frontend", "React", "What is Virtual DOM?", ["Copy of HTML DOM in memory", "Real DOM", "Database tree", "CSS Renderer"], "A"),
("Frontend", "React", "Props are?", ["Mutable", "Read-only", "Not required", "Functions"], "B"),
("Frontend", "React", "Which command creates a new React app?", ["react new", "create-react-app", "npm react", "react-create"], "B"),
("Frontend", "React", "Which hook replaces lifecycle methods?", ["useRef()", "useState()", "useEffect()", "useCallback()"], "C"),
("Frontend", "React", "Which hook is used for global state & data sharing?", ["useShare()", "useContext()", "useGlobal()", "useProp()"], "B"),
("Frontend", "React", "Default file extension for JSX?", [".js", ".jsx", ".html", ".tsx"], "B"),
("Frontend", "React", "Keys in lists help?", ["Uniqueness & diffing", "Sorting", "CSS styling", "Debugging"], "A"),
("Frontend", "React", "In React, data flows?", ["Both ways", "Two-way binding", "One-way downward", "Random"], "C"),
("Frontend", "React", "Which file represents entry point in CRA?", ["app.js", "index.js", "main.js", "home.js"], "B"),
("Frontend", "React", "Which renders UI in browser?", ["ReactDOM.render()", "Renderer()", "UI.create()", "React.render()"], "A"),
("Frontend", "React", "Which hook stores mutable DOM ref?", ["useState()", "useRef()", "useMemo()", "useDOM()"], "B"),
("Frontend", "React", "React is based on?", ["MVC", "OOP", "Component-based architecture", "None"], "C"),
("Frontend", "React", "State updates are?", ["Synchronous", "Asynchronous", "Manual only", "Not allowed"], "B"),
("Frontend", "React", "React Router enables?", ["Animations", "Database", "Page navigation", "Hooks"], "C"),
("Frontend", "React", "Fragments are created using?", ["<div>", "<frag>", "<Fragment>", "<>...</>"], "D"),
("Frontend", "React", "Which hook optimizes expensive calculations?", ["useMemo()", "useEffect()", "useReducer()", "useError()"], "A"),

]  # END of list

print("📝 Inserting questions...")

bulk_q = []
for category, topic, question, opts, ans in data:
    bulk_q.append(Question(
        category=category,
        topic=topic,
        question=question,
        option_a=opts[0],
        option_b=opts[1],
        option_c=opts[2],
        option_d=opts[3],
        correct_answer=ans,
        qtype="MCQ"
    ))

Question.objects.bulk_create(bulk_q)

print(f"✔ Successfully inserted {len(bulk_q)} questions 🎯🔥")
print("\nAll done! 🚀")
