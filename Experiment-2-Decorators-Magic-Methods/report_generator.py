import functools

# Experiment 2: Dynamic Report Generator using Decorators, Class Methods and Magic Methods

# ---------- Decorators ----------
def bold_text(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper


def log_generation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Generating report using: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} completed successfully.")
        return result
    return wrapper


# ---------- Report Class ----------
class Report:
    templates = {}          # class variable storing templates

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, func):
        cls.templates[name] = func
        print(f"Template added: {name}")

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = Report.get_template(template_name)
        if template is None:
            return f"Template '{template_name}' not found."
        return template(self)

    def __str__(self):
        return f"Report(Title: {self.title})"

    def __repr__(self):
        return f"Report(title={self.title!r}, content={self.content!r})"


# ---------- Template Functions ----------
@log_generation
def simple_template(report):
    return f"{report.title}\n{'-' * len(report.title)}\n{report.content}"


@log_generation
@bold_text
def fancy_template(report):
    return f"===== {report.title.upper()} =====\n{report.content}\n===== END ====="


# ---------- Main ----------
def main():
    print("=== DYNAMIC REPORT GENERATOR ===\n")

    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    report = Report("Monthly Sales Report",
                    "Total Sales: Rs. 1,50,000\nUnits Sold: 320\nGrowth: 12%")

    print("\nAvailable templates:", list(Report.templates.keys()))

    print("\n--- SIMPLE TEMPLATE ---")
    print(report("simple"))

    print("\n--- FANCY TEMPLATE ---")
    print(report("fancy"))

    print("\n--- MAGIC METHODS ---")
    print("str()  ->", str(report))
    print("repr() ->", repr(report))

    print("\n--- INVALID TEMPLATE ---")
    print(report("pdf"))


if __name__ == "__main__":
    main()
