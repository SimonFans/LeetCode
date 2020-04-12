Example:  

"Codility we test coders"  k=14

Result: "Codility we"


class solution():
    def crop_words(self,s, k):
        if not s or k <= 0: return ""
        all_words = s.split(" ")
        
        cropped_s = ""
        for w in all_words:
            temp_s = cropped_s+ w
            if len(temp_s) <= k:
                cropped_s = temp_s + " "
            else:
                break
        return cropped_s.rstrip()
    
    
print(solution().crop_words("  codility We test coders",14))
