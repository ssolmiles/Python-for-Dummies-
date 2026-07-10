
def dummy_summarize(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

dummy_summarize(1, 2, 4, name="Norwegian", age=19)