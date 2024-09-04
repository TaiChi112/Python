class MyDBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "app":
            return "sqlite"
        return 'default'
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == "app":
            return "sqlite"
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = self.db_for_read(obj1)
        db_obj2 = self.db_for_read(obj2)
        return db_obj1 == db_obj2
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "app":
            return db == "sqlite"
        return db == "default"