import urllib
import urllib2
import json

#helper function
class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

#helper function
def get_utf8(ip_list):
	return [item.encode('utf8',"replace") for item in ip_list]

#Gets the master data of our scope
#All details about california tribes and their artifacts

def get_master_data_subtribes():
	url = "https://apis.berkeley.edu/hearst_museum/select"
	values = {'q' : 'objculturetree_ss:California Tribes',
	            'rows' : '44800',
	            'wt' : 'json',
	            'indent': 'on',
	            'fl' : 'objculturetree_txt,objculturetree_ss,objassoccult_txt,objname_s,objdescr_s,objfilecode_ss,blob_ss'}

	headers = { 'app_id' : '8dc4e11c',
	            'app_key': '4aa1d8d78752ef675e607187c4663b17',
	            'User-Agent': 'Mozilla 5.10',
	            'Accept-Charset':'utf-8'}
	data = urllib.urlencode(values)
	url = url + '?' + data
	req = urllib2.Request(url, None, headers)

	result = urllib2.urlopen(req).read()
	r = Payload(result)
	#print "All cali artifcats = ", len(r.response['docs'])
	new_list = [item for item in r.response['docs'] if ("objculturetree_txt" in item.keys() and "objculturetree_ss" in item.keys() 
		and "blob_ss" in item.keys() and "objname_s" in item.keys() and "objdescr_s" in item.keys() and "objfilecode_ss" in item.keys() and "objassoccult_txt" in item.keys()) ]
	#print "Artifacts that have all fields:", len(new_list)
	return new_list

#Returns a list of all subtribes (each element is a string) under California Tribes
#Landing page dropdown

def get_sub_tribes():
	new_list = get_master_data_subtribes()
	#Clean up the data
	new_list_red = [item for item in new_list if '@California tribes' in item['objculturetree_txt']]
	#print "cali artifacts: ", len(new_list_red)
	subtribes_array = [item['objassoccult_txt'] for item in new_list_red]
	subtribes = list(set([item for sublist in subtribes_array for item in sublist]))
	subtribes_utf = get_utf8(subtribes)
	#print "Before removing dups: subtribes: ", len(subtribes_utf)
	subtribe_list = [item for item in subtribes_utf if (('@' not in  item) and ('DO NOT USE' not in item) and ('?' not in item) )]
	#print "Final length = ", len(subtribe_list)
	return subtribe_list

#Returns a list of all artifact objects of a specific subtribe
#Eg: Each element in the list is of type: {u'objname_s': u'Basket', u'objdescr_s': u'Twined, bowl shape.', u'blob_ss': [u'dadf1602-55c0-4d88-9fe6'], u'objfilecode_ss': [u'1.5 Household']}
def get_all_artifacts(tribe_name):
	url = "https://apis.berkeley.edu/hearst_museum/select"
	values = {'q' : 'objassoccult_txt:' + tribe_name,
	            'rows' : '44800',
	            'wt' : 'json',
	            'indent': 'on',
	            'fl' : 'objname_s,objdescr_s,objfilecode_ss,blob_ss'}

	headers = { 'app_id' : '8dc4e11c',
	            'app_key': '4aa1d8d78752ef675e607187c4663b17',
	            'User-Agent': 'Mozilla 5.10',
	            'Accept-Charset':'utf-8'}

	data = urllib.urlencode(values)
	url = url + '?' + data
	req = urllib2.Request(url, None, headers)

	result = urllib2.urlopen(req).read()
	r = Payload(result)
	#print "Total number of artifcats:", len(r.response['docs'])
	artifact_list = [item for item in r.response['docs'] if (("objname_s" in item.keys()) and ("objdescr_s" in item.keys()) and ("objfilecode_ss" in item.keys()) and ("blob_ss" in item.keys())) ]

	#print "After removing, Num artifacts", len(new_list)
	print type(artifact_list), type(artifact_list[0])
	return artifact_list

#Gives the url for the image
#Can be potentially used in the bootstrap elements - EXPLORE
def get_image_url(id_, size_, 
				base_url="https://dev.cspace.berkeley.edu/pahma_project/imageserver/blobs/",
				app_id='8dc4e11c', app_key='4aa1d8d78752ef675e607187c4663b17'):

    url = "{base_url}/{id}/derivatives/{derivative}/content?".format(base_url=base_url,id=id_,derivative=size_) + \
    urllib.urlencode({'app_id':app_id,
                      'app_key':app_key})
    return url

# Returns a jpeg image of the specified size in the same directory.
# supported image sizes: Thumbnail, Medium - both in jpeg format

def get_image_file(blob_id, blob_size):
	
	req = urllib2.Request(get_image_url(blob_id, blob_size), None)

	result = urllib2.urlopen(req).read()
	f = open('blob.jpeg','w')
	f.write(result)
	f.close()
	return f

def main():
	#get_master_data()
	get_sub_tribes()
	get_all_artifacts("Yurok")	
	#get_image('7664cd16-a8f0-4837-8163', 'Medium')

main()