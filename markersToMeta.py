#!/usr/bin/env python

# Created by: Moksh Chitkara
# Last Update: Mar 10th 2026
# v1.1.1
# Copyright (C) 2026  Moksh Chitkara
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import bisect

# Global Variables
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
colorLst = ['Blue','Cyan','Green','Yellow', 'Red','Pink','Purple','Fuchsia','Rose','Lavender','Sky','Mint','Lemon','Sand','Cocoa','Cream']
propLst = ['2nd Asst', '2nd Continuity', '2nd DIT', '2nd DOP', '2nd DOP Reviewed', '2nd Dir', '2nd Dir Asst', '2nd Dir Reviewed', '3D Rig ID #', '3D Rig Type', 'Alpha mode', 'Angle', 'Aspect Ratio Notes', 'Assistant Director', 'Assistant Producer', 'Audio Bit Depth', 'Audio Ch', 'Audio Codec', 'Audio Duration TC', 'Audio End TC', 'Audio FPS', 'Audio File Type', 'Audio Media', 'Audio Notes', 'Audio Offset', 'Audio Recorder', 'Audio Start TC', 'Audio TC Type', 'Aux 1', 'Aux 2', 'BG (m)', 'Bit Depth', 'Bit Rate', 'CDL SAT', 'CDL SOP', 'CV (m)', 'Calibration Source', 'Calibration Type', 'Calibration UUID', 'Camera #', 'Camera Aperture', 'Camera Aperture Type', 'Camera Assistant', 'Camera FPS', 'Camera Firmware', 'Camera Format', 'Camera ID', 'Camera Manufacturer', 'Camera Notes', 'Camera Operator', 'Camera Pan Angle', 'Camera Position', 'Camera Roll Angle', 'Camera Serial #', 'Camera TC Type', 'Camera Tilt Angle', 'Camera Type', 'Category', 'Clip Color', 'Clip Directory', 'Clip Name', 'Clip Number', 'Cloud Sync', 'Codec Bitrate', 'Color Chart', 'Color Space Notes', 'Colorist', 'Colorist Assistant', 'Colorist Notes', 'Colorist Reviewed', 'Comments', 'Compression Ratio', 'Continuity', 'Continuity Reviewed', 'Convergence Adj', 'Crew Comments', 'DOP', 'DOP Reviewed', 'Dailies Colorist', 'Data Level', 'Data Wrangler', 'Date Added', 'Date Created', 'Date Modified', 'Date Recorded', 'Day / Night', 'Deck Firmware', 'Deck Serial #', 'Description', 'Dialog Duration', 'Dialog Notes', 'Dialog Starts As', 'Digital Technician', 'Director', 'Director Reviewed', 'Distance', 'Drop frame', 'Duration', 'EDL Clip Name', 'Editing Assistant', 'Editor', 'Embedded Audio', 'Enable Deinterlacing', 'End', 'End Dialog TC', 'End TC', 'Environment', 'Episode #', 'Episode Name', 'FG (m)', 'FPS', 'FSD', 'Field Dominance', 'File Name', 'File Path', 'Filter', 'Flags', 'Focal Point (mm)', 'Focus Puller', 'Focus Reviewed', 'Format', 'Frames', 'Framing Chart', 'Gamma Notes', 'Genre', 'Good Take', 'Grey Chart', 'H-FLIP', 'IA (mm)', 'IDT', 'ILPD', 'ISO', 'Immersive ID', 'In', 'Input Color Space', 'Input LUT', 'Input Sizing Preset', 'Key Grip', 'Keyword', 'LUT 1', 'LUT 2', 'LUT 3', 'LUT Used', 'LUT Used On Set', 'Lab Roll #', 'Lens Chart', 'Lens Notes', 'Lens Number', 'Lens Type', 'Line Producer', 'Location', 'Media Type', 'Mon Color Space', 'Monitor LUT', 'Move', 'ND Filter', 'Noise Reduction', 'None', 'Offline Reference', 'Online Status', 'Out', 'PAR', 'PAR Notes', 'People', 'Post Producer', 'Producer', 'Production Asst', 'Production Company', 'Production Name', 'Program Name', 'Projection', 'Proxy', 'Proxy Media Path', 'RAW', 'Reel Name', 'Reel Number', 'Resolution', 'Reviewers Notes', 'Rig Inverted', 'Roll/Card', 'S3D Eye', 'S3D Notes', 'S3D Shot', 'S3D Sync', 'Safe Area', 'Sample Rate', 'Sample Rate (KHz)', 'Scene', 'Script Supervisor', 'Send to', 'Send to Studio', 'Sensor', 'Sensor Area Captured', 'Series #', 'Setup', 'Sharpness', 'Shoot Day', 'Shot', 'Shot During Ep', 'Shot Frame Rate', 'Shot Type', 'Shutter Angle', 'Shutter Speed', 'Shutter Type', 'Slate TC', 'Sound Mixer', 'Sound Reviewed', 'Sound Roll #', 'Start', 'Start Dialog TC', 'Start KeyKode', 'Start TC', 'Subcategory', 'SuperScale Noise Reduction', 'SuperScale Sharpness', 'Synced Audio', 'Take', 'Time-lapse Interval', 'Tone', 'Track 1', 'Track 10', 'Track 11', 'Track 12', 'Track 13', 'Track 14', 'Track 15', 'Track 16', 'Track 17', 'Track 18', 'Track 19', 'Track 2', 'Track 20', 'Track 21', 'Track 22', 'Track 23', 'Track 24', 'Track 3', 'Track 4', 'Track 5', 'Track 6', 'Track 7', 'Track 8', 'Track 9', 'Transcription Status', 'Type', 'Unit Manager', 'Unit Name', 'Uploaded From', 'Usage', 'V-FLIP', 'VFX Grey Ball', 'VFX Markers', 'VFX Mirror Ball', 'VFX Notes', 'VFX Shot #', 'VFX Svsr Reviewed', 'Video Codec', 'Wardrobe Reviewed', 'White Balance Tint', 'White Point (Kelvin)', 'Super Scale']

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
			# Checkbox to delete marker
			ui.HGroup({ 'Weight': 0 }, [
			    ui.VGap(),
			    ui.CheckBox({"ID": "delete_check", "Text": "Delete markers on move", "Checked": True}),
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
			"Geometry": [1500,500,700,250], # x-position, y-position, width, height
			}, 
			main_ui())

itm = window.GetItems() # Grabs all UI elements to be manipulated
################################################################################################
# Functions #
#############

# Given markers and timeline return list of matching clips
# input: markers [dict of markers], timeline [timeline item]
# output: matches [dict of markers]
def get_matches(timeline, track):

    markers = timeline.GetMarkers()
    matches = {}
    # if clip and tl are enabled append start/end to list
    if timeline.GetIsTrackEnabled("video",track):
        print("")
        
        track_items = timeline.GetItemListInTrack("video",track)
        prog = 0
        total = len(track_items)

        for item in track_items:
            prog += 1
            loading = "{:.2%}".format(float(prog)/float(total))
            itm['Start'].Text = "Matching Track {}: {}".format(track, loading)
            if item.GetClipEnabled() and item.GetStart():
                for frame_id in markers:
                    if markers[frame_id]["color"] == str(itm["color_combo"].CurrentText):
                        frame_match = int(frame_id) + int(timeline.GetStartFrame())
                        if (int(item.GetStart()) <= frame_match) and (frame_match < int(item.GetEnd())):
                            print("Match found at", frame_match)
                            matches[frame_match] = markers.pop(frame_id)
                            try:
                                media = item.GetMediaPoolItem()
                            except:
                                media = None
                            matches[frame_match].update({"media": media})
                            break
    return matches


# Apply metadata to clip based on timecode match and delete marker if successful
# input: markers [list of dicts by frame number], starts [list], ends [list], timeline [timeline item], track [int]
# output: None
def apply_meta(matches, timeline, track):

    prog = 0
    total = len(matches)
    for frame_id in sorted(matches):
        prog += 1
        loading = "{:.2%}".format(float(prog)/float(total))
        itm['Start'].Text = "Applying Track {}: {}".format(track, loading)
        
        print("\nWorking on", frame_id)
        
        matching_media = matches[frame_id]["media"]
        if matching_media != None:  # if there is a mediapool item that matches
            name_bool = False
            note_bool = False
            if matching_media.SetClipProperty(itm["name_combo"].CurrentText, matches[frame_id]["name"]):
                print("Name Metadata added from marker")
                name_bool = True
            if matching_media.SetClipProperty(itm["note_combo"].CurrentText, matches[frame_id]["note"]):   # if metadata is added 
                print("Note Metadata added from marker")
                note_bool = True
            print(itm["delete_check"].Checked, name_bool, note_bool)
            if itm["delete_check"].Checked and (name_bool or note_bool):
                timeline.DeleteMarkerAtFrame(frame_id - int(timeline.GetStartFrame()))  # delete the marker
                print("Marker deleted")

def _main(ev):

    itm['Start'].Enabled = False
    itm['Start'].Text = "Starting..."
    
    timeline = project.GetCurrentTimeline()

    # do a single track or all tracks
    try:
        dest_track = int(itm["track_edit"].Text)
        track_range = range(dest_track, dest_track + 1)
    except:
        track_range = reversed(range(1, timeline.GetTrackCount("video")+1))
    
    for track in track_range:
        matches = {}
        matches.update(get_matches(timeline, track))
        apply_meta(matches, timeline, track)
        
    itm['Start'].Text = "Move to Metadata"
    itm['Start'].Enabled = True
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
