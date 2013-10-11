#!/usr/bin/env python
#
##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###

# Convert videos to MP4.
#
# Convert video files to MP4, using ffmpeg.
#
# NOTE: This script requires Python and a recent version of ffmpeg.

##############################################################################
### OPTIONS                                                                ###

## FFmpeg

# Path to the ffmpeg binary.
#FFmpegPath=/usr/local/bin/ffmpeg

# Path to the ffprobe binary.
#FFprobePath=/usr/local/bin/ffprobe

## Conversion

# Extension for created file (m4v, mp4).
#MP4Extension=m4v

# Delete the original file (0, 1).
#DeleteOriginal=1

# Even convert MP4 files (0, 1).
#ConvertMP4=0

# Optimize created file - move MOOV atom to the start (0, 1).
#OptimizeForStreaming=1

## Audio

# Ensure that the audio will play on iOS (0, 1).
#iOSAudio=1

# Audio codec to be used.
#AudioCodec=libfdk_aac

# Options for audio codec.
#AudioOpts=-vbr 5

# Audio streams to copy.
#
# Three letter country code, blank for all.
#AudioLanguage=eng

# Lanuage for unknown audio.
#DefaultAudioLanguage=eng

# Subtitle streams to copy.
#
# Three letter country code, blank for all.
#SubtitleLanguage=eng

# Language for unknown subtitles.
#DefaultSubtitleLanguage=eng

# CRF value for HD encoding.
#x264CRF-HD=23

# CRF value for SD encoding.
#x264CRF-SD=21

# x264 Preset to use.
#x264Preset=medium

# Other x264 options.
#x264Opts=b-adapt=2

### NZBGET POST-PROCESSING SCRIPT                                          ###
##############################################################################


