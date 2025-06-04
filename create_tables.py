from app.database import Base, engine
import app.models  # para que SQLAlchemy conozca todas las clases de modelo

def main():
    # Crea todas las tablas que hayas definido en app.models (y en otros .py de modelos)
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente.")

if __name__ == "__main__":
    main()
