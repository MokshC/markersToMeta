#!/usr/bin/env python

# Created by: Moksh Chitkara
# Last Update: Mar 6th 2026
# v1.0.0
# Copyright (C) 2026  Moksh Chitkara
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bisect

# Global Variables
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
colorLst = ['Blue','Cyan','Green','Yellow', 'Red','Pink','Purple','Fuchsia','Rose','Lavender','Sky','Mint','Lemon','Sand','Cocoa','Cream']
propLst = ['2nd Asst', '2nd Continuity', '2nd DIT', '2nd DOP', '2nd DOP Reviewed', '2nd Dir', '2nd Dir Asst', '2nd Dir Reviewed', '3D Rig ID #', '3D Rig Type', 'Alpha mode', 'Angle', 'Aspect Ratio Notes', 'Assistant Director', 'Assistant Producer', 'Audio Bit Depth', 'Audio Ch', 'Audio Codec', 'Audio Duration TC', 'Audio End TC', 'Audio FPS', 'Audio File Type', 'Audio Media', 'Audio Notes', 'Audio Offset', 'Audio Recorder', 'Audio Start TC', 'Audio TC Type', 'Aux 1', 'Aux 2', 'BG (m)', 'Bit Depth', 'Bit Rate', 'CDL SAT', 'CDL SOP', 'CV (m)', 'Calibration Source', 'Calibration Type', 'Calibration UUID', 'Camera #', 'Camera Aperture', 'Camera Aperture Type', 'Camera Assistant', 'Camera FPS', 'Camera Firmware', 'Camera Format', 'Camera ID', 'Camera Manufacturer', 'Camera Notes', 'Camera Operator', 'Camera Pan Angle', 'Camera Position', 'Camera Roll Angle', 'Camera Serial #', 'Camera TC Type', 'Camera Tilt Angle', 'Camera Type', 'Category', 'Clip Color', 'Clip Directory', 'Clip Name', 'Clip Number', 'Cloud Sync', 'Codec Bitrate', 'Color Chart', 'Color Space Notes', 'Colorist', 'Colorist Assistant', 'Colorist Notes', 'Colorist Reviewed', 'Comments', 'Compression Ratio', 'Continuity', 'Continuity Reviewed', 'Convergence Adj', 'Crew Comments', 'DOP', 'DOP Reviewed', 'Dailies Colorist', 'Data Level', 'Data Wrangler', 'Date Added', 'Date Created', 'Date Modified', 'Date Recorded', 'Day / Night', 'Deck Firmware', 'Deck Serial #', 'Description', 'Dialog Duration', 'Dialog Notes', 'Dialog Starts As', 'Digital Technician', 'Director', 'Director Reviewed', 'Distance', 'Drop frame', 'Duration', 'EDL Clip Name', 'Editing Assistant', 'Editor', 'Embedded Audio', 'Enable Deinterlacing', 'End', 'End Dialog TC', 'End TC', 'Environment', 'Episode #', 'Episode Name', 'FG (m)', 'FPS', 'FSD', 'Field Dominance', 'File Name', 'File Path', 'Filter', 'Flags', 'Focal Point (mm)', 'Focus Puller', 'Focus Reviewed', 'Format', 'Frames', 'Framing Chart', 'Gamma Notes', 'Genre', 'Good Take', 'Grey Chart', 'H-FLIP', 'IA (mm)', 'IDT', 'ILPD', 'ISO', 'Immersive ID', 'In', 'Input Color Space', 'Input LUT', 'Input Sizing Preset', 'Key Grip', 'Keyword', 'LUT 1', 'LUT 2', 'LUT 3', 'LUT Used', 'LUT Used On Set', 'Lab Roll #', 'Lens Chart', 'Lens Notes', 'Lens Number', 'Lens Type', 'Line Producer', 'Location', 'Media Type', 'Mon Color Space', 'Monitor LUT', 'Move', 'ND Filter', 'Noise Reduction', 'Offline Reference', 'Online Status', 'Out', 'PAR', 'PAR Notes', 'People', 'Post Producer', 'Producer', 'Production Asst', 'Production Company', 'Production Name', 'Program Name', 'Projection', 'Proxy', 'Proxy Media Path', 'RAW', 'Reel Name', 'Reel Number', 'Resolution', 'Reviewers Notes', 'Rig Inverted', 'Roll/Card', 'S3D Eye', 'S3D Notes', 'S3D Shot', 'S3D Sync', 'Safe Area', 'Sample Rate', 'Sample Rate (KHz)', 'Scene', 'Script Supervisor', 'Send to', 'Send to Studio', 'Sensor', 'Sensor Area Captured', 'Series #', 'Setup', 'Sharpness', 'Shoot Day', 'Shot', 'Shot During Ep', 'Shot Frame Rate', 'Shot Type', 'Shutter Angle', 'Shutter Speed', 'Shutter Type', 'Slate TC', 'Sound Mixer', 'Sound Reviewed', 'Sound Roll #', 'Start', 'Start Dialog TC', 'Start KeyKode', 'Start TC', 'Subcategory', 'SuperScale Noise Reduction', 'SuperScale Sharpness', 'Synced Audio', 'Take', 'Time-lapse Interval', 'Tone', 'Track 1', 'Track 10', 'Track 11', 'Track 12', 'Track 13', 'Track 14', 'Track 15', 'Track 16', 'Track 17', 'Track 18', 'Track 19', 'Track 2', 'Track 20', 'Track 21', 'Track 22', 'Track 23', 'Track 24', 'Track 3', 'Track 4', 'Track 5', 'Track 6', 'Track 7', 'Track 8', 'Track 9', 'Transcription Status', 'Type', 'Unit Manager', 'Unit Name', 'Uploaded From', 'Usage', 'V-FLIP', 'VFX Grey Ball', 'VFX Markers', 'VFX Mirror Ball', 'VFX Notes', 'VFX Shot #', 'VFX Svsr Reviewed', 'Video Codec', 'Wardrobe Reviewed', 'White Balance Tint', 'White Point (Kelvin)', 'Super Scale']

################################################################################################
# Window creation #
###################
def main_ui():
	# vertical group
	window = [ui.VGroup({"Spacing": 15,},[
			# horizontal groups
			# Marker Selection
			ui.HGroup({"Spacing": 3}, [ 	
				ui.Label({"ID": "color_label","Text": "Use markers of color: "}),
				ui.ComboBox({"ID": "color_combo"})
			]),
			# Name
			ui.HGroup({"Spacing": 3}, [ 
				ui.Label({"ID": "name_label","Text": "Set marker name to: "}),	
				ui.ComboBox({"ID": "name_combo"})
			]),
			# Note
			ui.HGroup({"Spacing": 3}, [ 
				ui.Label({"ID": "note_label","Text": "Set marker note to: "}),	
				ui.ComboBox({"ID": "note_combo"})
			]),
			# Track Select
			ui.HGroup({ 'Weight': 0 }, [
				ui.Label({ 'Text': "Set metdata on following track: " }),
				ui.LineEdit({ 'ID': "track_edit", "PlaceholderText": "Leave empty for top clip"}),
			]),
			# button for export
			ui.Button({"ID": "Start", "Text": "Move to Metadata", "Weight": 0}),
			]) 
		]
	return window

ui = fu.UIManager # get UI utility from fusion
disp = bmd.UIDispatcher(ui) # gets display settings?

# window definition
window = disp.AddWindow({"WindowTitle": "Markers to Metadata",
			"ID": "MTMWin", 
			'WindowFlags': {'Window': True,'WindowStaysOnTopHint': True},
			"Geometry": [1500,500,700,200], # x-position, y-position, width, height
			}, 
			main_ui())

itm = window.GetItems() # Grabs all UI elements to be manipulated
################################################################################################
# Functions #
#############

# Given a start frame on timeline returns media pool item
# input: start_value [int], timeline [timeline item], track [int]
# output: media pool item
def get_media_by_start(start_value, timeline, track):
    for item in timeline.GetItemListInTrack("video", track):
        if item.GetStart() == start_value:
            return item.GetMediaPoolItem()
    return None  # Return None if no item with the given start value is found

# Given a track and timeline return starts and ends of all items on that track
# input: track [int], timeline [timeline item]
# output: starts [list], ends [list]
def get_starts_ends(track, timeline):
    starts = []
    ends = []
    # if clip and tl are enabled append start/end to list
    if timeline.GetIsTrackEnabled("video",track):
        for item in timeline.GetItemListInTrack("video",track):
            try:
                if item.GetClipEnabled():
                    starts.append(int(item.GetStart()))
                    ends.append(int(item.GetEnd()))
            except:
                pass
    return sorted(starts), sorted(ends)

# Apply metadata to clip based on timecode match and delete marker if successful
# input: markers [list of dicts by frame number], starts [list], ends [list], timeline [timeline item], track [int]
# output: None
def apply_meta(markers, starts, ends, timeline, track):

    for frame_id in sorted(markers):
        if markers[frame_id]["color"] == str(itm["color_combo"].CurrentText):
            # Use binary search to find the index of the first item whose start is greater than frameId
            start_index = bisect.bisect_right(starts, int(frame_id) + int(timeline.GetStartFrame()))
            # Check timeline items where the frameId is within their range
            for index in range(start_index):
                if frame_id <= ends[index]: # If frameId is within the timeline item's end
                    print("Clip Match found at timeline frame", starts[index])
                    matching_media = get_media_by_start(starts[index], timeline, track)
                    if matching_media != None:  # if there is a mediapool item that matches
                        if matching_media.SetClipProperty(itm["name_combo"].CurrentText, markers[frame_id]["name"]) and matching_media.SetClipProperty(itm["note_combo"].CurrentText, markers[frame_id]["note"]):   # if metadata is added 
                            print("Metadata added from marker\n")
                            timeline.DeleteMarkerAtFrame(frame_id)  # delete the marker
                    break

def _main(ev):
    timeline = project.GetCurrentTimeline()

    # do a single track or all tracks
    try:
        dest_track = int(itm["track_edit"].Text)
        track_range = range(dest_track, dest_track + 1)
    except:
        track_range = reversed(range(1, timeline.GetTrackCount("video")+1))
    
    for track in track_range:
        markers = timeline.GetMarkers()
        starts, ends = get_starts_ends(track, timeline) # needed for binary search that happens in apply_meta
        apply_meta(markers, starts, ends, timeline, track)
    
# needed to close window
def _close(ev):
	disp.ExitLoop()

################################################################################################
# GUI Elements #
# manipulations
itm['name_combo'].AddItems([propLst[88]] + propLst[:88] + propLst[89:]) # adds items to dropdown
itm['note_combo'].AddItems([propLst[70]] + propLst[:70] + propLst[71:]) # adds items to dropdown
itm['color_combo'].AddItems(colorLst)   # adds items to dropdown
# button presses
window.On.Start.Clicked = _main
window.On.MTMWin.Close = _close
window.Show()
disp.RunLoop()
window.Hide()
#################################################################################################
