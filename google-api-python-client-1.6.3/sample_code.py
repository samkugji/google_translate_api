#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Translate.

Command-line application that translates some text.
"""
from __future__ import print_function
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

import os

def main():

  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./data/translate-72c6ff2e1ec8.json"
  credentials = GoogleCredentials.get_application_default()

  service = build('translate', 'v2',
            credentials=credentials)
  print(service.translations().list(
      source='kor',
      target='jpn',
      q=['감자', '원피스']
    ).execute())

if __name__ == '__main__':
  main()
