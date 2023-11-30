import React from 'react';
interface SocialMediaHandle {
  name: string;
  url: string;
}
interface ProfileCardProps {
  socialMediaHandles?: SocialMediaHandle[]; // Make the prop optional
}
const ProfileCard: React.FC<ProfileCardProps> = ({ socialMediaHandles }) => {
  return (
    <div className="bg-white rounded-lg shadow p-4">
      {/* Profile picture */}
      <div className="w-24 h-24 rounded-full bg-gray-300"></div>
      {/* Name */}
      <h2 className="text-xl font-bold mt-4">John Doe</h2>
      {/* Bio */}
      <p className="text-gray-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      {/* Social media handles */}
      {socialMediaHandles && socialMediaHandles.length > 0 && (
        <div className="flex mt-2">
          {socialMediaHandles.map((handle, index) => (
            <a key={index} href={handle.url} className="mr-2 text-blue-500">
              {handle.name}
            </a>
          ))}
        </div>
      )}
    </div>
  );
};
export default ProfileCard;