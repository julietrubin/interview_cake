class Rectangle():
	def __init__(self, start_pointx, end_pointx, start_pointy, end_pointy):
		self.x = start_pointx
		self.y = start_pointy
		self.width = end_pointx - start_pointx
		self.height = end_pointy - start_pointy
	
def line_intersection(start_point1, end_point1, start_point2, end_point2):
	if start_point1 <= start_point2 and start_point2 <= end_point1:
		return start_point2, min(end_point1, end_point2)
	return None, None
	
def intersection_rectangle(rec1, rec2):
	start_pointx, end_pointx = line_intersection(
		rec1.x, rec1.x + rec1.width, rec2.x, rec2.x + rec2.width)
	if start_pointx == None:
		start_pointx, end_pointx = line_intersection(
			rec2.x, rec2.x + rec2.width, rec1.x, rec1.x + rec1.width)
	if start_pointx == None:
		# there is no x intersection 
		return new Rectangle()
	start_pointy, end_pointy = line_intersection(
		rec1.y, rec1.y + rec1.height, rec2.y, rec2.y + rec2.height)
		
	if start_pointy == None;
		start_pointy, end_pointy = line_intersection(
			rec2.y, rec2.y + rec2.height, rec1.y, rec1.y + rec1.height)
			
	if start_pointy == None:
		# there is no y intersection
		return new Rectangle()
	
	rec = new Rectangle(start_pointx, end_pointx, start_pointy, end_pointy)
	return rec