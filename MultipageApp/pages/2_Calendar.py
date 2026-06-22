import numpy as np ; import math
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys ; import os ; import glob
import timeit
from PIL import Image
import datetime
from timezonefinder import TimezoneFinder ; import pytz
import streamlit as st

import astropy
import astropy.units as u
import astropy.time as at
from astropy.io import fits
from astropy.wcs import WCS
from astropy.utils.data import get_pkg_data_filename
import astropy.utils.data as aud
from astropy.coordinates import SkyCoord, AltAz, EarthLocation, get_body
import astropy.coordinates as ac
import astropy.constants as constants

import astroquery.jplhorizons as jpl
from astroquery.simbad import Simbad
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive as NEA
from astroquery.vizier import Vizier

from astroplan import FixedTarget, Observer
import astroplan as ap
import astroplan.plots as app
from astroplan.plots import plot_sky

from ics import Calendar, Event

from Utility import Render_Sidebar, Generate_Calendar

st.set_page_config(layout="wide")

st.logo("official-logo.png", size = "large", link = "https://philsa.gov.ph") 

Render_Sidebar()

############################################################################

st.subheader('Generate Calendars')
st.caption("This function produces an .ics file for users to import in their calendar (Gmail and/or Outlook Calendar) for their planning purposes.")
st.divider(width = 'stretch')

############################################################################

if 'TDates' not in st.session_state:
    st.warning('No transit data found. Please go back and submit the form first.')
    st.stop()

TDates = st.session_state['TDates']
st.dataframe(TDates) 

############################################################################

# Generate_Calendar(TDates)

############################################################################
