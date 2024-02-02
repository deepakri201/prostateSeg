FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-runtime

RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y libxrender-dev

RUN cd ..
RUN pip install scikit-learn
RUN pip install scikit-image
RUN pip install Pillow
RUN pip install matplotlib
RUN pip install numpy
RUN pip install pandas
RUN pip install monai==1.0.1
RUN pip install nibabel
RUN pip install tensorboard
RUN pip install itk
RUN pip install tqdm
RUN pip install torchvision
RUN pip install matplotlib
RUN pip install einops
RUN pip install SimpleITK~=2.1.0
RUN pip install pyyaml
RUN pip install munch
RUN pip install pydicom
RUN pip install pyarrow
RUN pip install fire
RUN pip install ignite
RUN pip install pytorch-ignite