FROM python:3.10.14-bookworm

RUN pip install --upgrade pip

COPY /drug_molecule_gen /app/drug_molecule_gen

WORKDIR /app

RUN pip install -r drug_molecule_gen/requriments.txt

ENV PYTHONPATH=${PYTHONPATH}:/app/drug_molecule_gen

RUN chmod +x drug_molecule_gen/train_pipeline.py

RUN chmod +x drug_molecule_gen/predict.py

ENTRYPOINT [ "python3" ]

CMD [ "./drug_molecule_gen/train_pipeline.py" ]
