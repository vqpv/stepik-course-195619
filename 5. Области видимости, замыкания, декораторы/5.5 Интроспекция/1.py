def get_info_about_object(obj):
    attr_m = dir(obj)
    print(attr_m)
    print(f"Всего у объекта {len(attr_m)} атрибутов и методов")
