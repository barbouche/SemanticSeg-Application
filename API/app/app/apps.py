
from django.apps import AppConfig
from dependencies.scripts_male_voice.hparams import create_hparams
from dependencies.scripts_male_voice.model import Tacotron2
from dependencies.scripts_male_voice.layers import TacotronSTFT, STFT
from dependencies.scripts_male_voice.audio_processing import griffin_lim
from dependencies.scripts_male_voice.train import load_model
from dependencies.scripts_male_voice.denoiser import Denoiser
from dependencies.scripts_models.hubconf import nvidia_waveglow, nvidia_tacotron2
from dependencies.scripts_voice_clonning.synthesizer.inference import Synthesizer
from dependencies.scripts_voice_clonning.encoder import inference as encoder
from dependencies.scripts_voice_clonning.vocoder import inference as vocoder
import os
import torch
from pathlib import Path

class ModelConfig(AppConfig):
    pass
    # #Nessaisre to map with the app 
    # name = 'nvidia'
    # #Import waveglow chekpoint && model
    # print('########################################',torch.cuda.get_device_capability())
    # print('########################################', torch.cuda.is_initialized())
    # print('########################################', torch.cuda.get_device_name())
    # waveglow = nvidia_waveglow()
    # waveglow = waveglow.remove_weightnorm(waveglow)
    # waveglow = waveglow.to('cuda') 
    # waveglow.eval()   
    # #Import tacotron2 chekpoint && model
    # tacotron2 = nvidia_tacotron2()
    # tacotron2 = tacotron2.to('cuda')
    # tacotron2.eval()
    # #Create hparams to changing audio settings rate for using in male voice
    # hparams = create_hparams()
    # #New Value of the hyperparameter seted
    # hparams.sampling_rate = 22050
    # #Import chekpoint for male voice
    # checkpoint_path = "/home/docker/app/dependencies/checkpoints/checkpoint_19000.pth"
    # #Load model with updating hyperparpeter
    # model = load_model(hparams)
    # #Charge chekpoint within model
    # model.load_state_dict(torch.load(checkpoint_path)['state_dict'])
    # _ = model.eval()
    # denoiser = Denoiser(waveglow)
    # #Load clonning model
    # encoder_weights = Path("/home/docker/app/dependencies/checkpoints/pretrained.pt")
    # vocoder_weights = Path("/home/docker/app/dependencies/checkpoints/pretrained_vocoder.pt")
    # syn_dir = Path("/home/docker/app/dependencies/checkpoints/")
    # encoder.load_model(encoder_weights)
    # synthesizer = Synthesizer(syn_dir)
    # vocoder.load_model(vocoder_weights)
    # #

