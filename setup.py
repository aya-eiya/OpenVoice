from setuptools import setup, find_packages


setup(name='gen_voice_model',
      version='0.0.0',
      description='Instant voice cloning by MyShell.',
      long_description=open('README.md').read().strip(),
      long_description_content_type='text/markdown',
      keywords=[
            'text-to-speech',
            'tts',
            'voice-clone',
            'zero-shot-tts'
      ],
      url='https://github.com/aya-eiya/OpenVoice',
      project_urls={
        'Documentation': 'https://github.com/aya-eiya/OpenVoice/blob/main/docs/USAGE.md',
        'Changes': 'https://github.com/aya-eiya/OpenVoice/releases',
        'Code': 'https://github.com/aya-eiya/OpenVoice',
        'Issue tracker': 'https://github.com/aya-eiya/OpenVoice/issues',
      },
      author='MyShell',
      author_email='ethan@myshell.ai',
      license='MIT License',
      packages=find_packages(),

      python_requires='>=3.9',
      install_requires=[
            'librosa==0.11.0',
            'faster-whisper==1.1.1',
            'pydub==0.25.1',
            'wavmark==0.0.3',
            'numba==0.61.2',
            'numpy==2.2.6',
            'eng_to_ipa==0.0.2',
            'inflect==7.5.0',
            'unidecode==1.4.0',
            'openai-whisper @ git+https://github.com/openai/whisper.git',
            'whisper-timestamped==1.15.8',
            'openai==1.88.0',
            'python-dotenv',
            'pypinyin==0.54.0',
            'cn2an==0.5.23',
            'jieba==0.42.1',
            'gradio==5.34.2',
            'langid==1.1.6',
      ],
      zip_safe=False
      )
