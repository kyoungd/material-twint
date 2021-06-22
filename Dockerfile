FROM continuumio/miniconda:latest

WORKDIR /home/docker_conda_template

COPY . .
COPY twint twint
COPY elasticsearch elasticsearch
RUN echo "pip install ./twint" > ~/.bashrc

RUN conda env create -f environment.yml

RUN echo "source activate base_twint" > ~/.bashrc
ENV PATH /opt/conda/envs/baseapi/bin:$PATH


EXPOSE 8101

ENTRYPOINT ["python"]
CMD ["app.py"]
