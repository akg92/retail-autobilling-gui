import pickle as pk
file_name = 'detection_results.pkl'
with open(file_name,'rb') as f:
 data = pk.load(f)

score = 0.5
def get_all_cats(img_id,labels):
 global score
 anns = labels.getAnnIds([img_id])
 result = []
 for ele in anns:
  if 'score' in labels.anns[ele]:
   if labels.anns[ele]['score']>score:
    result.append(labels.anns[ele]['category_id'])
  else:
   result.append(labels.anns[ele]['category_id'])
 return sorted(result)


v_counts = 0
cocoGt = data.cocoGt
cocoDt = data.cocoDt

def calculate(s):
 global score,v_counts
 score = s
 v_counts = 0
 for key in cocoDt.imgs.keys():
  valid = True
  ann_gt = get_all_cats(key, cocoGt)
  ann_dt = get_all_cats(key, cocoDt)
  #print(len(ann_gt))
  #print(len(ann_dt))
  #print("#######")
  if len(ann_gt)==len(ann_dt):
   i = 0
   while(i<len(ann_gt)):
    if ann_gt[i] !=ann_dt[i]:
     break
    i+=1
   #print(i%len(ann_gt))
   if i==len(ann_gt):
    v_counts+=1
 print(v_counts/24000)
